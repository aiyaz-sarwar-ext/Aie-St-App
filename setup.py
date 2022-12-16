import os
from datetime import datetime
from setuptools import find_packages
from setuptools import setup  




setup(
    name="aie-st-app",
    version=os.getenv("APP_VERSION"),
    description="this package contains a simple streamlit app",
    long_description="maintained by ai enablement team",
    author="AI Enablement",
    author_email="aienablementticket@bayer.com",
    install_requires=["streamlit", "PyYAML", "pyjwt[crypto]","pandas","boto3","smart_open"],
    #install_requires=[PyP for PyP in req_txt.split("\n")], # Python Package/Distribution
    #python_requires=">=3.7, <3.8",
    packages=find_packages(),
    package_data={"aie-st-app": ["bucket.yaml"]},
)

