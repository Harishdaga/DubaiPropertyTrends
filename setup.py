from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path):
    """
    This function return list of requirements.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


    
setup(
    name='dubai_analysis',
    version='0.0.1',
    author='Harish Daga',
    author_email='mrharishdaga@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)