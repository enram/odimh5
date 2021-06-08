# odimh5

[![.github/workflows/run-tests.yaml](https://github.com/enram/odimh5/actions/workflows/run-tests.yaml/badge.svg)](https://github.com/enram/odimh5/actions/workflows/run-tests.yaml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A simple Python package to access data in [ODIM HDF5](https://www.eumetnet.eu/wp-content/uploads/2019/01/ODIM_H5_v23.pdf) format.

Limitations:

- (currently) read-only
- Python 3.7+

# Tutorial

## Install from PyPI

    $ pip install odimh5

# Development instructions

## Install the local package

    $ pip install -e .

## Install dev dependencies

    $ pip install -r requirements.txt

## Run tests

    $ pytest
    $ mypy odimh5

## Format code

    $ black .

## Generate and upload a new version

1) Update version number in `setup.py`
2) Make sure everything is commited 
3) Build the package:

```
$ python3 -m build
```

4) Upload it to PyPI:

```
$ python3 -m twine upload dist/*
```

5) Tag it:
   
```
$ git tag v0.1.0
$ git push origin --tags
```
    


