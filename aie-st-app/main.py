import datetime
import jwt
import os
from pathlib import Path
import streamlit as st
from streamlit.web.server.websocket_headers import _get_websocket_headers
import sys
import yaml
import botocore
import boto3
from smart_open import smart_open
import pandas as pd

class StApp:

    def __init__(self, name_yaml: str = "bucket.yaml", server_port: int = None) -> None:
        self.here = str(Path(__file__).parent.absolute())
        self.name = name_yaml
        self.path = "".join([str(self.here), "/", self.name])
        self.port = server_port
        self.headers = _get_websocket_headers()
        self.aad_user_jwt =  self.headers.get("X-Amzn-Oidc-Data")
        self.support = "aienablementticket@bayer.com"
        
    def decode_jwt(self, jwt_in: str) -> dict[str, str]:
        """
        Decode jwt from header key X-Amzn-Oidc-Data
        """
        decoded = jwt.decode(jwt_in, options={"verify_signature": False})
        return decoded


    def main(self) -> int:
        """
        Simple streamlit app that parse an input yaml and displays the content.
        And also displays current user.
        """
        user_decoded = self.decode_jwt(jwt_in=self.aad_user_jwt)
        user_email = user_decoded.get("email")
        st.markdown(f"# Hello {user_email}")
        st.markdown("# Welcome to AI Enablement Streamlit App")
        st.markdown(f"This app is maintained by the AI Enablement team. Ai Enablement uses the app for testing the streamlit cicd pipeline and developing and documenting of new features. [Here](https://gitlab.bayer.com/ai-enablement/aie-st-app/-/tree/development) you can access the source code of the app. If you do not have access, please contact us {self.support}")
        st.markdown("## How To Identify User for Personalization")
        
        st.markdown("Install required python packages. Be aware that this solution only works for streamlit==1.14.0 and above. We recommend to create a virtual environment.")
        st.code("pip install pyjwt[crypto] streamlit", "bash")

        st.markdown("Next step is to access the web socket headers and extract jwt that carry user data.")
        st.code("""import jwt \n
import streamlit as st \n
from streamlit.web.server.websocket_headers import _get_websocket_headers""", "python")
        st.markdown("Access web socket headers and display them.")
        st.code("""headers = _get_websocket_headers() \n
# Display headers object in streamlit app \n
st.write("Web socket header data:") \n
st.write(headers)""", "python")
        st.write("Web socket header data:")
        st.write(self.headers)
        
        st.markdown("Decode jwt to access user data.")
        st.code("""jwt_user_data = headers.get("X-Amzn-Oidc-Data")\n
user_decoded = jwt.decode(jwt_user_data, options={"verify_signature": False})\n
st.write("Decoded user data from 'X-Amzn-Oidc-Data'.")\n
st.write(user_decoded)""", "python")
        st.write("Decoded user data from 'X-Amzn-Oidc-Data'.")
        st.write(user_decoded)

        st.markdown("Select user data needed for your application.")
        st.code("""user_email = user_decoded.get("email")\n
st.write(f"Welcome {user_email}!")""", "python")
        user_email = user_decoded.get("email")
        st.write(f"Welcome {user_email}!")
        st.write("The current time is:")
        now = datetime.datetime.now()
        st.write(str(now))

        with open(self.path) as file:
            try:
                bucket_config = yaml.safe_load(file)
                st.markdown("## Display content of a yaml file, that is part of the wheel")
                st.write("My config file: ")
                st.write(bucket_config)

            except yaml.YAMLError as exec:
                print(exec)
                raise
        st.markdown("## Provide meta data to endusers")
        st.write("It is best practice to provide a contact email.")
        st.markdown(f"#### Contact: {self.support}")
         # Set when app is deployed to k8s cluster
        st.markdown("Also, it is recommended to display the current version of your app. In IZ-QA and IZ-PROD, the deployed version is set as an environment variable `WHEEL_VERSION`")
        st.code("""import os\n
import streamlit as st\n        
version = os.getenv('WHEEL_VERSION', "NOT_SET_IN_EZ_BY_DEFAULT")\n
st.markdown(f"#### Version: {version}")""", "python")
        
        
        #import plotly.express as px
        st.code("""client = boto3.client('s3')\n

def upload_to_aws(local_file, bucket, s3_file):\n
    print("###", local_file, bucket, s3_file)\n
    s3 = boto3.client('s3')\n

    try:\n
        s3.upload_file(local_file, bucket, s3_file)\n
        print("Upload Successful")\n
        return True\n
    except FileNotFoundError:   \n   
        print("The file was not found")\n
        return False\n
    except NoCredentialsError:\n
        print("Credentials not available")\n
        return False\n

def read_file(bucket_name,file_to_be_read):\n
    with smart_open('s3://' + bucket_name + '/' + file_to_be_read, 'rb') as s3_source:\n
        s3_source.seek(0)  # seek to the beginning\n
        message = s3_source.read(1000000)\n
    return (message.decode('utf8'))\n

st.set_page_config(layout="wide")\n
st.title("Interact with s3 buckets")\n

#df = pd.read_csv("Data/gapminder_tidy.csv")\n

st.markdown('Currently only 'france-dsci-app' bucket has Read Write permissions from IZ ')\n
s3_bucket_env = list(['phmsbi-cpd-analytics-dev','phmsbi-cpd-analytics-prod','france-dsci-app','dsaa-cph-ai-s3-qa','dsaa-cph-ai-s3-dev','dsaa-cph-ai-s3-prod','dsaa-cph-ai-cdp-landing-zone'])\n
metric_list = list(['read','write a text to a file','copy the file'])\n

s3_bucket_env = st.selectbox(label = "Choose a bucket", options = s3_bucket_env)\n
metric = st.selectbox(label = "Choose a metric", options = metric_list)\n

st.write('You selected:', s3_bucket_env)\n
st.write('You selected:', metric)\n

if metric == 'write a text to a file':\n
    text_to_put = st.text_input('Enter text : ')\n
    key_to_write_to = st.text_input('Enter Key to write to : ')\n
    client.put_object( \n
    Bucket= s3_bucket_env,\n
    Body= text_to_put,\n
    Key= key_to_write_to)\n

elif metric == 'copy the file' :\n
    uploaded_file = st.file_uploader("Choose a txt/csv file", accept_multiple_files=True)\n
    key_to_write_to = st.text_input('Enter Key to write to : ')\n
    dataframe = pd.read_csv(uploaded_file)\n
    upload_to_aws(uploaded_file, s3_bucket_env, key_to_write_to)\n

elif metric == 'read':\n
    file_name = st.text_input('Enter File Name : ')\n
    file_content = read_file(s3_bucket_env,file_name)\n
    st.write('The content of the file is ', file_content)""","python")


        
        client = boto3.client('s3')

        #Working and correctly uploading the file in s3 bucket
        def upload_to_aws(local_file, bucket, s3_file):
            print("###", local_file, bucket, s3_file)
            s3 = boto3.client('s3')

            try:
                s3.upload_file(local_file, bucket, s3_file)
                print("Upload Successful")
                return True
            except FileNotFoundError:      
                print("The file was not found")
                return False
            except NoCredentialsError:
                print("Credentials not available")
                return False

        def read_file(bucket_name,file_to_be_read):
            with smart_open('s3://' + bucket_name + '/' + file_to_be_read, 'rb') as s3_source:
                s3_source.seek(0)  # seek to the beginning
                message = s3_source.read(1000000)
            return (message.decode('utf8'))

        st.set_page_config(layout="wide")
        st.title("Interact with s3 buckets")

        #df = pd.read_csv("Data/gapminder_tidy.csv")
        st.markdown('Currently only 'france-dsci-app' bucket has Read Write permissions from IZ ')
        s3_bucket_env = list(['phmsbi-cpd-analytics-dev','phmsbi-cpd-analytics-prod','france-dsci-app','dsaa-cph-ai-s3-qa','dsaa-cph-ai-s3-dev','dsaa-cph-ai-s3-prod','dsaa-cph-ai-cdp-landing-zone'])
        metric_list = list(['read','write a text to a file','copy the file'])

        s3_bucket_env = st.selectbox(label = "Choose a bucket", options = s3_bucket_env)
        metric = st.selectbox(label = "Choose a metric", options = metric_list)

        st.write('You selected:', s3_bucket_env)
        st.write('You selected:', metric)

        if metric == 'write a text to a file':
            text_to_put = st.text_input('Enter text : ')
            key_to_write_to = st.text_input('Enter Key to write to : ')
            client.put_object( 
            Bucket= s3_bucket_env,
            Body= text_to_put,
            Key= key_to_write_to)

        elif metric == 'copy the file' :
            uploaded_file = st.file_uploader("Choose a txt/csv file", accept_multiple_files=True)
            key_to_write_to = st.text_input('Enter Key to write to : ')
            dataframe = pd.read_csv(uploaded_file)
            upload_to_aws(uploaded_file, s3_bucket_env, key_to_write_to)

        elif metric == 'read':
            file_name = st.text_input('Enter File Name : ')
            file_content = read_file(s3_bucket_env,file_name)
            st.write('The content of the file is ', file_content)
    
        st.markdown(f"#### Version: {os.getenv('WHEEL_VERSION', 'NOT_SET_IN_EZ_BY_DEFAULT')}")

        return 0
    
    def main_cli(self) -> None:
        """
        This function can be used by setup.py to create a shell command via entrypoint.
        """
        os.system(f"streamlit run {__file__} --server.port {self.port}")

if __name__ == "__main__":
    app = StApp()
    raise SystemExit(app.main())
