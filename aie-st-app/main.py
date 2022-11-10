import datetime
from pathlib import Path
import os
import streamlit as st
import sys
import yaml


class StApp:

    def __init__(self, name_yaml: str = "bucket.yaml", server_port: int = None) -> None:
        self.here = str(Path(__file__).parent.absolute())
        self.name = name_yaml
        self.path = "".join([str(self.here), "/", self.name])
        self.port = server_port

    def main(self) -> None:
        """Simple streamlit app that parse an input yaml and displays the content."""
        
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
    
    def main_cli(self) -> int:
        """This function can be used by setup.py to create a shell command."""
        os.system(f"streamlit run {__file__} --server.port {self.port}")

if __name__ == "__main__":
    app = StApp()
    raise SystemExit(app.main())
