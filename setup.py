from setuptools import setup
from typing import List



# Declearing variable for setup functions
PROJECT_NAME="housing_predictor"
VERSION="0.0.3"
AUTHOR="Pourush Kumar Gupta"
DESCRIPTION="This is my first machine learning project"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement mention
    in requirement.txt file

    This function is going to return a list of all the libraries mentions in 
    requirement.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requires=get_requirements_list()
)

