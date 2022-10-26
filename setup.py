from datetime import datetime
from setuptools import find_packages
from setuptools import setup  

setup(
    name="aie-st-app",
    version=datetime.now().strftime("%Y.%m.%d"),
    description="this package contains a simple streamlit app",
    long_description="maintained by ai enablement team",
    author="AI Enablement",
    author_email="aienablementticket@bayer.com",
    install_requires=["streamlit", "PyYAML"],
    packages=find_packages(),
    package_data={"aie-st-app": ["bucket.yaml"]},
)

