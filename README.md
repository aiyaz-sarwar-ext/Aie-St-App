# aie-demo-st

Kind of hello world streamlit app. Can be used as a template for projects that want to pack the whole streamlit application into a wheel. This setup also allows to include config files (.yml, etc) into your wheel. Be aware that the meaning of __package__ in python terms is not very accurate to describe a wheel.


## Installation

`pip install --index-url "https://sai-sai-transient:<secret-token>@artifactory.bayer.com/artifactory/api/pypi/sai-pypi-prod-packagestore/simple" aie-st-app`


## CI

This project also demonstrates a basic ci routine. Including testing (pytest and pre-commit-hooks, not implemeted but definetly go for it) and building and pushing the wheel to bayer artifactory. To access `sai-pypi-prod-packagestore` (hosted on https://artifactory.bayer.com/ui/login/) please contact aienablementticket@bayer.com.


## Entrypoints

Might be implemented in the future, however none of the current streamlit apps uses this feature fo their wheel.


## TODO

1) Explore https://setuptools.pypa.io/en/latest/index.html to learn more about packaging.
2) Instead of `setup.py` use `setup.cfg`
3) For entrypoint make the port dynamic, currently hard coded to 8093.

## Read Further

Want to learn more about Bayer artifactory?
- Documentation -> https://docs.int.bayer.com/cloud/devops/artifactory/?utm_source=legacy-redirect&utm_medium=url
- AI Enablement How-To's -> TDB
