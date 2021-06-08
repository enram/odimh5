# odim_h5

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A simple Python package to access data in [ODIM HDF5](https://www.eumetnet.eu/wp-content/uploads/2019/01/ODIM_H5_v23.pdf) format 

Limitations:

- (currently) read-only
- Python 3.7+

# Development

## Install locally

    $ pip install -e .

## Install dev dependencies

    $ pip install -r requirements.txt

## Run tests

    $ pytest
    $ mypy odim_h5

## Format code

    $ black .

