"""Behavior specification for the first pure Semantic Kernel primitive."""
import copy
from dataclasses import FrozenInstanceError, replace
import unittest
from uuid import UUID, uuid4
from semantic_kernel.public import SemanticElementId, SemanticElementIdError

VALID = "sem_550e8400-e29b-41d4-a716-446655440000"
OTHER = "sem_550e8400-e29b-41d4-a716-446655440001"


class SemanticElementIdTests(unittest.TestCase):
    def assert_invalid(self, value, code):
        for operation in (SemanticElementId, SemanticElementId.parse):
            with self.subTest(value=value, operation=operation):
                with self.assertRaises(SemanticElementIdError) as caught:
                    operation(value)
                self.assertEqual(caught.exception.code, code)
                self.assertIsInstance(caught.exception, ValueError)
        self.assertIsNone(SemanticElementId.try_parse(value))

    def test_valid_constructor_and_parse_share_contract(self):
        self.assertEqual(SemanticElementId(VALID), SemanticElementId.parse(VALID))
        self.assertEqual(SemanticElementId(VALID).value, VALID)

    def test_empty_null_and_whitespace_have_empty_diagnostic(self):
        for value in (None, "", " ", "\t\n", "\u2003"):
            self.assert_invalid(value, "SEM-ID-001")

    def test_unsupported_input_representations_are_not_coerced(self):
        for value in (False, True, 0, 123, b"identifier", [], {}, UUID(VALID[4:]), object()):
            self.assert_invalid(value, "SEM-ID-003")

    def test_invalid_text_shapes_have_format_diagnostic(self):
        for value in ("not-an-id", "sales.Customer", "tenant_type_v1_123", "sem_", VALID[:-1], VALID + "0", VALID[4:], VALID.replace("-", ""), "sem_{" + VALID[4:] + "}", "sem_urn:uuid:" + VALID[4:]):
            self.assert_invalid(value, "SEM-ID-002")

    def test_prefix_is_strict_and_hex_is_case_insensitive(self):
        uppercase_hex = "sem_" + VALID[4:].upper()
        mixed = "sem_550E8400-e29B-41D4-A716-446655440000"
        self.assertEqual(str(SemanticElementId.parse(uppercase_hex)), VALID)
        self.assertEqual(SemanticElementId.parse(mixed), SemanticElementId(VALID))
        for value in ("SEM_" + VALID[4:], "type_" + VALID[4:], "sem-" + VALID[4:]):
            self.assert_invalid(value, "SEM-ID-002")

    def test_fixed_length_boundaries_and_hex_extremes(self):
        for value in ("sem_00000000-0000-4000-8000-000000000000", "sem_ffffffff-ffff-4fff-bfff-ffffffffffff"):
            self.assertEqual(len(str(SemanticElementId(value))), 40)
        self.assert_invalid("sem_00000000-0000-0000-0000-000000000000", "SEM-ID-002")
        self.assert_invalid("sem_ffffffff-ffff-ffff-ffff-ffffffffffff", "SEM-ID-002")

    def test_version_bits_must_be_four_and_are_never_repaired(self):
        for version in "012356789abcdef":
            self.assert_invalid(VALID[:18] + version + VALID[19:], "SEM-ID-002")

    def test_rfc_variant_bits_accept_only_eight_nine_a_b(self):
        for variant in "89abAB":
            value = VALID[:23] + variant + VALID[24:]
            self.assertEqual(SemanticElementId(value).value[23], variant.lower())
        for variant in "01234567cdef":
            self.assert_invalid(VALID[:23] + variant + VALID[24:], "SEM-ID-002")

    def test_wrong_separators_invalid_ascii_unicode_and_controls(self):
        for value in (VALID.replace("-", "_"), VALID[:-1] + "g", VALID[:-1] + "/", VALID[:-1] + "\x00", VALID.replace("5", "５", 1), VALID.replace("-", "−", 1), VALID[:-1] + "é"):
            self.assert_invalid(value, "SEM-ID-002")

    def test_leading_and_trailing_whitespace_are_rejected_without_trimming(self):
        for value in (" " + VALID, VALID + " ", VALID + "\n", "\t" + VALID, VALID[:10] + " " + VALID[11:]):
            self.assert_invalid(value, "SEM-ID-002")

    def test_equal_ids_have_equal_hash_and_work_as_dictionary_keys(self):
        left, right = SemanticElementId(VALID), SemanticElementId("sem_" + VALID[4:].upper())
        self.assertEqual(left, right)
        self.assertEqual(hash(left), hash(right))
        self.assertEqual({left: "definition"}[right], "definition")
        self.assertEqual(len({left, right}), 1)

    def test_different_ids_are_unequal(self):
        self.assertNotEqual(SemanticElementId(VALID), SemanticElementId(OTHER))
        self.assertEqual(len({SemanticElementId(VALID), SemanticElementId(OTHER)}), 2)

    def test_id_is_not_a_raw_string_uuid_or_other_category(self):
        identity = SemanticElementId(VALID)
        self.assertNotEqual(identity, VALID)
        self.assertNotEqual(VALID, identity)
        self.assertNotEqual(identity, UUID(VALID[4:]))
        self.assertNotEqual(identity, None)

    def test_value_cannot_be_assigned_or_deleted(self):
        identity = SemanticElementId(VALID)
        with self.assertRaises(FrozenInstanceError):
            identity.value = OTHER
        with self.assertRaises(FrozenInstanceError):
            del identity.value
        self.assertFalse(hasattr(identity, "__dict__"))
        self.assertEqual(str(identity), VALID)

    def test_copy_and_deepcopy_keep_identity_and_replacement_validates(self):
        identity = SemanticElementId(VALID)
        self.assertEqual(copy.copy(identity), identity)
        self.assertEqual(copy.deepcopy(identity), identity)
        self.assertEqual(replace(identity), identity)
        with self.assertRaises(SemanticElementIdError):
            replace(identity, value="invalid")

    def test_string_and_safe_parse_round_trip(self):
        identity = SemanticElementId(VALID)
        self.assertEqual(SemanticElementId.parse(str(identity)), identity)
        self.assertEqual(SemanticElementId.try_parse(str(identity)), identity)
        self.assertEqual(SemanticElementId.try_parse(VALID).value, VALID)

    def test_standard_uuid4_output_is_accepted_without_kernel_generation(self):
        for _ in range(128):
            raw = "sem_" + str(uuid4())
            identity = SemanticElementId.parse(raw)
            self.assertEqual(str(identity), raw)
            self.assertEqual(UUID(raw[4:]).version, 4)

    def test_errors_have_stable_code_without_echoing_external_input(self):
        secret = "sensitive-external-input"
        with self.assertRaises(SemanticElementIdError) as caught:
            SemanticElementId.parse(secret)
        self.assertIn("SEM-ID-002", str(caught.exception))
        self.assertNotIn(secret, str(caught.exception))
        self.assertNotIn(secret, repr(caught.exception))

    def test_string_subclass_cannot_override_normalization_to_invalid_state(self):
        class MisleadingString(str):
            def lower(self):
                return "invalid"
            def isspace(self):
                return True
        identity = SemanticElementId(MisleadingString(VALID))
        self.assertEqual(identity.value, VALID)
        self.assertIs(type(identity.value), str)

    def test_safe_parse_does_not_swallow_unexpected_implementation_errors(self):
        class BrokenId(SemanticElementId):
            def __post_init__(self):
                raise RuntimeError("Unexpected implementation error")
        with self.assertRaises(RuntimeError):
            BrokenId.try_parse(VALID)

    def test_missing_constructor_argument_is_programmer_misuse(self):
        with self.assertRaises(TypeError):
            SemanticElementId()

    def test_rename_does_not_change_identity(self):
        identity = SemanticElementId(VALID)
        definition = {"id": identity, "name": "sales.Customer"}
        definition["name"] = "sales.Client"
        self.assertIs(definition["id"], identity)
        self.assertEqual(str(definition["id"]), VALID)
