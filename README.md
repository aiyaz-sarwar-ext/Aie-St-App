# aie-demo-st

Kind of hello world streamlit app. Can be used as a template for projects that want to pack the whole streamlit application into a wheel. This setup also allows to include config files (.yml, etc) into your wheel. Be aware that the meaning of __package__ in python terms means a folder that contains an `__init__.py`. However, here we will use it also to describe a wheel file that can be installed from a PyPI repository, more fitting name would probably be distribution, but we are used to say package.

## Notes for streamlit developers

- Streamlit App source code must be stored in a folder (python package) named after the name of the app. All lowercase and only dashes are allowed. Example: `my-awful-app`

- The top level of your python package must contain a `main.py` file, which when given as a parameter to streamlit cli `streamlit run main.py` will start your streamlit app.

```python3
my-awful-app
    main.py
```

- Inside your python package you need to create an empty `__init__.py` file. Also in all sub directories you need to create `__init__.py` files.

```python3
my-awful-app
    subdir1
        __init__.py
    subdir2
        __init__.py
    main.py
    __init__.py
```

- If you parse config files or want to display images these files also have to be stored inside your python package. If you do not stroe them inside the python package these files won't be included inside the wheel and your application will probably not behave or look as you expect.

```python3
my-awful-app
    image_dir
        awful001.png
        awful002.png
        beautiful001.png
    config_dir
        config.json
    subdir1
        __init__.py
    subdir2
        __init__.py
    main.py
    __init__.py
    config.yaml
```
- If your code needs to access files, the complete path to the files is required to ensure the code is properly executed.

```python3
import pathlib

# getting the path of the current directory and storing it in the variable "here"
here = pathlib.Path(__file__).parent.absolute()

#converting the variable "here" to a string and adding the name of the file that needs to be accessed
logo = str(here) + "/" + "bayer_logo.png"
```

- If you have dependencies we recommend to use pip dependency resolver.
  1) Create a virtual environment and upgrade pip.
  2) Create a requirements.in file containing all your dependencies _without_ version. Pip will figure it out.
  3) Run 'pip freeze > requirements.txt' to generate your `requirements.txt` file.
  4) Please pin the python versions which must be used to run your application. Please list them in the `README.md`.
  5) `requirements.txt` file has to be stored outside of the python package at the top level of your repository.

```python3
my-awful-app
requirements.txt
README.md
```

- For versioning you can choose your own scheme, however we recommend the format `YYYY.mm.dd`

- For further questions regarding structuring your streamlit project repository please rich out to Ai Enablement via aienablementticket@bayer.com.

## Notes for using `setup.py`

- In general as a streamlit app developer you can configure your own setup.py or reach out to AI Enablement to get help.
- To learn more about python packaging with setuptools please use this resource https://setuptools.pypa.io/en/latest/index.html 
- Instead of using `setup.py` it is perfectly fine to either use `setup.cfg` or the most recent `pyproject.toml`.
- For pinning python version in `setup.py`:
```python3
setup(
 python_requires=">=3.7, <3.8", # Package can only be used in Python3.7
)

setup(
 python_requires=">=3.7", # Package can only be used in Python3.7 or more recent versions (3.8, 3.9 , ...)
)
```


## Installation

`pip install --extra-index-url "https://sai-sai-transient:<secret-token>@artifactory.bayer.com/artifactory/api/pypi/sai-pypi-prod-packagestore/simple" aie-st-app`

`--extra-index-url` flag is key here. Because only the aie-st-app wheel can be found there, but dependencies need to be fetched from another source. That is why we do not use `--index-url` flag, to keep default PyPI index as wheel source.

## CI

This project also demonstrates a basic ci routine. Including testing (pytest and pre-commit-hooks, not implemeted but definetly go for it) and building and pushing the wheel to bayer artifactory. To access `sai-pypi-prod-packagestore` (hosted on https://artifactory.bayer.com/ui/login/) please contact aienablementticket@bayer.com.


## Entrypoints

Might be implemented in the future, however none of the current streamlit apps uses this feature fo their wheel.



## Read Further

Want to learn more about Bayer artifactory?
- Documentation -> https://docs.int.bayer.com/cloud/devops/artifactory/?utm_source=legacy-redirect&utm_medium=url
- AI Enablement How-To's -> TDB
