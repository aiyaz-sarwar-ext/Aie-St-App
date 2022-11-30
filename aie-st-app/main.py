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
        user = self.decode_jwt(jwt_in=self.aad_user_jwt).get("email") 
        st.title(f"Welcome {user}!")
        st.title('Hello World!')
        st.title("Current date and time: ")
        now = datetime.datetime.now()
        st.title(str(now))

        with open(self.path) as file:
            try:
                bucket_config = yaml.safe_load(file)
                st.title("My config file: ")
                st.title(bucket_config)

                st.title("Contact: aienablementticket@bayer.com")
                # Set when app is deployed to k8s cluster
                st.title(f"Version: {os.getenv('WHEEL_VERSION')}")

            except yaml.YAMLError as exec:
                print(exec)
                raise
        st.write("Web socket header data:")
        st.write(self.headers)

        return 0
    
    def main_cli(self) -> None:
        """
        This function can be used by setup.py to create a shell command via entrypoint.
        """
        os.system(f"streamlit run {__file__} --server.port {self.port}")

if __name__ == "__main__":
    app = StApp()
    raise SystemExit(app.main())
