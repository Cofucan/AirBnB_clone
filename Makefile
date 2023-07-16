.PHONY: executable

executable:
	chmod +x $(shell find . -name "*.py")

pycodestyle:
	pycodestyle $(shell find ./models -name "*.py")