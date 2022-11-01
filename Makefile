dist: ## builds source and wheel package
    python3 setup.py sdist bdist_wheel

clean-build: ## remove build artifacts
    rm -fr build/
    rm -fr dist/
    rm -fr .eggs/

test: ## run tests quickly with the default Python
    pytest

release: dist ## package and upload a release
    twine upload dist/*


# clean: ## remove all build, test, coverage and Python artifacts
# clean-build: ## remove build artifacts
# clean-pyc: ## remove Python file artifacts
# clean-test: ## remove test and coverage artifacts
# lint: ## check style with flake8
# test: ## run tests quickly with the default Python
# test-all: ## run tests on every Python version with tox
# release: ## package and upload a release
# dist: ## builds source and wheel package
# install: ## install the package to the active Python's site-packages