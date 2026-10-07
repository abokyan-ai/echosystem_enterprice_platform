PYTHON ?= python3

.PHONY: install build test test-architecture doctor lint dependencies check-architecture
install build test doctor lint dependencies:
	$(PYTHON) scripts/dev.py $@

test-architecture:
	$(PYTHON) scripts/dev.py test:architecture

check-architecture:
	$(PYTHON) scripts/dev.py check:architecture
