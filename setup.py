from setuptools import setup
from typing import List


# Declearing variable for setup functions
PROJECT_NAME="housing_predictor"
VERSION="0.0.1"
AUTHOR="pourush kumar gupta"
DESCRIPTION="This is my first machine learning project"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list():
    """
    Description: This function is going to return list of requirement mention
    in requirement.txt file

    This function is going to return a list of all the libraries mentions in 
    requirement.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()
    


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requires=get_requirements_list()
)

