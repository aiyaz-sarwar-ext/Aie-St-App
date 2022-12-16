Delivery Sheet
==============

It is recommended to create a virtual environment and activate it:

    python -m venv .venv
    . .venv/bin/activate

The next step is the installation of sphinx

    pip install sphinx

and texlive to generate the pdf.

    sudo apt-get install texlive-full

Afterwards you can generate the pdf file by executing the bash script:

    bash make.sh

All files will be generated in the build directory. You can copy the .pdf file to the sheets directory. This way delivery sheets for all releases are stored and versioned in a separate directory.

Deployment Process
================
The AI Enablement team is responsible for the deployment of the streamlit application. The deployment process is started by creating a ticket at AI ENablement, containing only the version of your application to be deployed. After creating a ticket, AI Enablement will check the app repository for the delivery sheet. If the delivery sheet contains the required informatin for deployment, the app will be deployed on IZ QA. After the developer confirmed that the app works as expected, the process will be finished by deploying the app on IZ PROD. This delivery sheet contains all required information and an overview about the state of the application. 

Structure of the Delivery Sheet
==========
devops.rst (Notes for DevOps Team)
----------------------------------
This part contains required information for the deployment process and allows the AI Enablement team to quickly deploy the apps.

description.rst (Application Description)
-----------------------------------------
This section describes the business case for the application and elaborates the provided value to the business user.
Developers are encouraged to adjust this section properly. Every streamlit app is unique and therefore may require more contextual information. Creators can add subsections and show the impact and importance of the designed application. 

release.rst (Release)
---------------------
Specific information about the current release can be added here.

installation.rst (Installation Guide)
-------------------------------------
This guide should describe how the app should be installed locally and which requirements are necessary to run it succesfully.

dependencies.rst (Dependencies)
-------------------------------
The artifacts the proper execution of the app relies on. They could be different in dev, QA and Prod.

configuration.rst (Configuration)
----------------------------------
Guideline to configure the runtime of the product. Paths, config files, env variables, docker images, ....

uat.rst (User Acceptance Tests)
--------------------------------
Description of UATs if available.

testing.rst (Testing)
---------------------
Documentation of all steps and measures taken to t4est the product.

changelog.rst (Change Log)
--------------------------
The change log of all releases ( not the internal git log of the product ).

Other Files
===========
There is a kedro.csv, as an example. It comes from the nightly run of airflow.


Release Number
==============

this could change. As for some other python packages, (regex,...) the choice is :

    YYYY.mm.dd

this is easy to trace, self incrementing, ...

