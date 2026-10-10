from dataclasses import FrozenInstanceError
import unittest
from semantic_kernel.public import SemanticVersion, SemanticVersionError


class SemanticVersionTests(unittest.TestCase):
    def test_valid_versions_and_canonical_components(self):
        for text in ('0.0.0', '0.1.0', '1.0.0', '1.2.3', '10.20.30'):
            with self.subTest(text=text):
                version = SemanticVersion.parse(text)
                self.assertEqual((version.major, version.minor, version.patch), tuple(map(int, text.split('.'))))
                self.assertEqual(str(version), text)
                self.assertEqual(SemanticVersion.parse(str(version)), version)
                self.assertEqual(SemanticVersion.try_parse(text), version)

    def test_structured_constructor_is_canonical(self):
        self.assertEqual(str(SemanticVersion(1, 2, 3)), '1.2.3')

    def test_required_diagnostics(self):
        for value in (None, '', ' ', '\t\n'):
            with self.subTest(value=value), self.assertRaises(SemanticVersionError) as caught:
                SemanticVersion.parse(value)
            self.assertEqual(caught.exception.code, 'SEM-VER-001')

    def test_rejected_syntax_and_types(self):
        for value in ('1', '1.0', 'v1.0.0', '01.0.0', '1.01.0', '1.0.01', '-1.0.0', '1.-1.0', '1.0.-1', '1.0.0.0', '1..0', '1.0.x', '1.0.0 ', ' 1.0.0', '1.0.0\n', '１.0.0', '١.0.0', '+1.0.0', '1e2.0.0', '1_000.0.0', 123, True, [], {}, SemanticVersion(1, 0, 0)):
            with self.subTest(value=value), self.assertRaises(SemanticVersionError) as caught:
                SemanticVersion.parse(value)
            self.assertEqual(caught.exception.code, 'SEM-VER-002')
            self.assertIsNone(SemanticVersion.try_parse(value))

    def test_no_ranges_selectors_prerelease_or_build_metadata(self):
        for value in ('latest', 'current', 'stable', 'head', '*', '^1.0.0', '~1.0.0', '>=1.0.0', '1.0.0 - 2.0.0', '1.0.0-alpha', '1.0.0+build.123'):
            with self.subTest(value=value), self.assertRaises(SemanticVersionError):
                SemanticVersion.parse(value)

    def test_component_validation_rejects_bool_subclasses_floats_and_negatives(self):
        class IntSubclass(int):
            pass
        for index in range(3):
            for bad in (-1, True, False, 1.0, '1', None, IntSubclass(1), 2**63):
                parts = [1, 2, 3]
                parts[index] = bad
                with self.subTest(index=index, bad=bad), self.assertRaises(SemanticVersionError) as caught:
                    SemanticVersion(*parts)
                self.assertEqual(caught.exception.code, 'SEM-VER-003')
                self.assertEqual(caught.exception.component_index, index)

    def test_portable_integer_boundary_and_oversized_input(self):
        maximum = 2**63 - 1
        self.assertEqual(SemanticVersion.parse(f'{maximum}.{maximum}.{maximum}'), SemanticVersion(maximum, maximum, maximum))
        for index in range(3):
            for bad in (str(2**63), '9' * 5000):
                parts = ['0', '0', '0']
                parts[index] = bad
                with self.subTest(index=index), self.assertRaises(SemanticVersionError) as caught:
                    SemanticVersion.parse('.'.join(parts))
                self.assertEqual(caught.exception.code, 'SEM-VER-003')
                self.assertEqual(caught.exception.component_index, index)

    def test_value_equality_and_hashing(self):
        a = SemanticVersion(1, 2, 3)
        b = SemanticVersion.parse('1.2.3')
        self.assertEqual(a, b)
        self.assertEqual(hash(a), hash(b))
        self.assertEqual({a: 'snapshot'}[b], 'snapshot')
        self.assertNotEqual(a, SemanticVersion(1, 2, 4))
        self.assertNotEqual(a, '1.2.3')
        self.assertNotEqual(a, (1, 2, 3))

    def test_numeric_ordering_including_lexical_trap(self):
        texts = ('0.0.0', '1.0.0', '1.0.1', '1.0.9', '1.1.0', '1.9.0', '1.9.9', '1.10.0', '2.0.0')
        versions = [SemanticVersion.parse(text) for text in texts]
        self.assertEqual(sorted(reversed(versions)), versions)
        for lower, upper in zip(versions, versions[1:]):
            self.assertLess(lower, upper)
            self.assertGreater(upper, lower)
            self.assertLessEqual(lower, upper)
            self.assertGreaterEqual(upper, lower)
        self.assertLessEqual(versions[0], versions[0])
        self.assertGreaterEqual(versions[0], versions[0])
        with self.assertRaises(TypeError):
            versions[0] < '1.0.0'

    def test_frozen_components(self):
        version = SemanticVersion(1, 2, 3)
        for field in ('major', 'minor', 'patch'):
            with self.assertRaises(FrozenInstanceError):
                setattr(version, field, 9)
        self.assertFalse(hasattr(version, '__dict__'))

    def test_try_parse_propagates_unexpected_errors(self):
        class Broken(SemanticVersion):
            def __post_init__(self):
                raise RuntimeError('unexpected')
        with self.assertRaises(RuntimeError):
            Broken.try_parse('1.0.0')

    def test_string_subclass_cannot_override_parsing(self):
        class Tricky(str):
            def split(self, *args):
                return ['1', '0', '0']
            def __str__(self):
                return '1.0.0'
        self.assertEqual(SemanticVersion.parse(Tricky('2.1.0')), SemanticVersion(2, 1, 0))
        self.assertIsNone(SemanticVersion.try_parse(Tricky('invalid')))

    def test_diagnostic_explains_format_without_retaining_input(self):
        with self.assertRaises(SemanticVersionError) as caught:
            SemanticVersion.parse('private-token')
        self.assertIn('major.minor.patch', caught.exception.message)
        self.assertIn('1.0.0', caught.exception.message)
        self.assertNotIn('private-token', str(caught.exception))
