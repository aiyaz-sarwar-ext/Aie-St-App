delivery sheet
==============

here are the documents to generate a delivery sheet. You will need to install sphinx

    pip install sphinx

and texlive to generate the pdf

    sudo apt-get install texlive-full

to generate the pdf file :

    bash make.sh

files will be generated in the build directory. Upload it and give it to recipients

integration team
================
The integration team is the people who take your delivery, deploy it in QA, run UAT tests, and then deploy it to prod.
They pull delivery from you, you don't push to them. This delivery sheet should contain all the information they need to
deploy your product

what to do
==========
- release.rst
put here description of things specific to this release
- installation.rst
everything the integration team should do to install your product
- dependencies.rst
the artefacts you depend on. They could be different in dev, QA and Prod.
- configuration.rst
how to configure the runtime of the product. Paths, config files, env variables, docker images, ....
- uat.rst
user acceptance test. What the user will do to consider your delivery is valid
- testing.rst
what you did to test your product
- changelog.rst
the change log of the deliveries ( not the internal git log of the product )

other files
===========
There is a kedro.csv, as an example. It comes from the nightly run of airflow.


release number
==============

this could change. As for some other python packages, (regex,...) the choice is :

    YYYY.mm.dd

this is easy to trace, self incrementing, ...



@todo : automation
==================

- this should be triggered by gitlab cicd.
- when pushed to master
- have a confluence token to upload the pdf file automatically
