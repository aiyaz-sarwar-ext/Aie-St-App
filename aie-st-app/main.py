import datetime
import jwt
import os
from pathlib import Path
import streamlit as st
from streamlit.web.server.websocket_headers import _get_websocket_headers
import sys
import yaml


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
