from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="odimh5",
    version="0.1.0",  # Following https://semver.org/
    description="A Python package to read ODIM HDF5 files",
    long_description=long_description,
    author="Nicolas Noé - INBO",
    author_email="nicolas.noe@inbo.be",
    url="https://github.com/enram/odimh5",
    packages=["odimh5"],
    python_requires=">3.7.0",
    install_requires=[  # Installation dependencies, let's keep development dependencies in requirements.txt
        "h5py>=3.1.0",
        "pytz",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
