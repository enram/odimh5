from distutils.core import setup

setup(
    name="odim_h5",
    version="0.1.0",  # Following https://semver.org/
    description="A Python package to read ODIM HDF5 files",
    author="Nicolas Noé - INBO",
    author_email="nicolas.noe@inbo.be",
    packages=["odim_h5"],
    python_requires=">3.7.0",
    install_requires=[  # Installation dependencies, let's keep development dependencies in requirements.txt
        "h5py>=3.1.0",
        "pytz",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
