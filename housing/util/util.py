import yaml 
from housing.exception import HousingException
import os,sys

def real_yaml_file(file_path:str)->str:
    """
    Reads a YAML file and return the contents of the dictonary. 
    file_path :str
    
    """
    try:
        with open(file_path,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e,sys) from e