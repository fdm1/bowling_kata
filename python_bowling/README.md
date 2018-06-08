[![Build Status](https://travis-ci.org/fdm1/python_skeleton.svg?branch=master)](https://travis-ci.org/fdm1/python_skeleton)

Python Skeleton Package
=======================

# Getting Started

Clone this repo and make it your own:

```
git clone https://github.com/fdm/python_skeleton <YOUR PROJECT NAME>
cd <YOUR PROJECT NAME>
./bin/setup_project.sh <YOUR GIT USERNAME> <YOUR PROJECT NAME>
```

Don't forget to update the readme and project specifics in `setup.py`.


Testing
=======
A testing framework is already in place for `pytest` and `pylint`, orchestrated through `tox`.

To run tests:
```
pip install tox
tox
```

A `.travis.yml` is also included so that you can just enable the repo for instant CI on [Travis CI](https://travis-ci.org).

