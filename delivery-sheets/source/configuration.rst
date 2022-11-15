Configuration
=============

The configuration shall be captured in a single yaml file.

YAML input :

.. literalinclude:: ../../bucket.yaml
  :language: yml
  :linenos:

Specifying bucket input files; Airflow path for ETL data (such as veeva, gers ...), suggestion path for suggestions and specific aie-st-app path for model data 

.. warning::

    For ETL Data airflow is ok , but model data should not be taken from Airflow since the model should not be re-trained every day without data scientist validation

Run
===

The product can be run after building the docker image (see in installation in dockerfile) as follows:

.. code-block::

    sudo docker run -d -p 8093:8501 -v ~/aie-st-app/:/app streamlit main.py

With this command the container would be started and the app would be visible in:

.. code-block::

    https://jupyter.devdsa3.ez.sats.cloud/custom4/

When starting the container from the docker image, the app is run by the following command (see dockerfile):

.. code-block::

    streamlit run aie-st-app/main.py
