from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path)-> list:
    '''
    this function will return the list of requirements
     mentioned in requirements.txt file
    '''
    requirements=[]
    
    with open(file_path, 'r') as file_object:
        requirements = file_object.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements
    

setup(
    name='ml-project',
    version='0.0.1',
    author='Balaji',
    author_email='sayabalaji@gmmmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
)