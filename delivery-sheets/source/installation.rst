Installation Guide
==================

Build Docker Image
------------------

Build docker image with the dockerfile in the same directory:

.. code-block::

    sudo docker build -f Dockerfile -t streamlit_aie-st-app .

The dockerfile is based on python 3.7 and will use the requirements.txt file to install all important python modules in the image.



Data files
----------

The app use S3 Bucket files parquet/csv from airflow, aie-st-app and suggestion keys

.. code-block::

    s3://phmsbi-cpd-analytics-dev/airflow
    s3://phmsbi-cpd-analytics-dev/cph_se/suggestion


to the deployment bucket. The two files are specified in the yaml file (see below).
