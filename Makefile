PYTHON ?= python3

.PHONY: install build test test-architecture doctor lint
install build test doctor lint:
	$(PYTHON) scripts/dev.py $@

test-architecture:
	$(PYTHON) scripts/dev.py test:architecture
