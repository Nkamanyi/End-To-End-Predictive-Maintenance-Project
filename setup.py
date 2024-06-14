from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    hyphen_e = "-e ."
    with open(file_path, 'r') as file:
        requirements = [line.strip() for line in file]
        if hyphen_e in requirements:
            requirements.remove(hyphen_e)
    return requirements

setup(
    name='predictive-maintenance-mlproject',
    version='0.0.1',
    author='Nkamanyi Martin',
    author_email='nkamanyimartin@gmail.com',
    description='A predictive maintenance machine learning project',
    long_description=open('README.md').read(), 
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    python_requires='>=3.6',  
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
