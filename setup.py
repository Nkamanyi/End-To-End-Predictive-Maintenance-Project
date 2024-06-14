from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path: str) -> List[str]:

    hyphen_e = "-e ."
    with open(file_path, 'r') as file:
        requirements = [line.strip() for line in file]
        if hyphen_e in requirements:
            requirements.remove(hyphen_e)
        return requirements

setup(
    name= 'predictive-maintenance-mlproject',
    version= '0.0.1',
    author= 'Nkamanyi Martin',
    author_email= 'nkamanyimartin@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')

)