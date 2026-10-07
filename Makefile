PYTHON ?= python3

.PHONY: install build test test-architecture doctor lint dependencies check-architecture fitness
install build test doctor lint dependencies fitness:
	$(PYTHON) scripts/dev.py $@

test-architecture:
	$(PYTHON) scripts/dev.py test:architecture

check-architecture:
	$(PYTHON) scripts/dev.py check:architecture
