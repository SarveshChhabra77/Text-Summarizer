from setuptools import setup,find_packages
from typing import List


def get_requirements(file_name:str)->List[str]:
    
    requirements = []
    
    try:
        
        with open(file_name,'r') as file_obj:
            lines = file_obj.readlines()
            
            for line in lines:
                requirement = line.strip()
                
                if requirement and requirement!='-e .':
                    requirements.append(requirement
                                        )
    except FileNotFoundError:
        print('requirements.txt file not found')
        
    return requirements




setup(
    name='Text-Summarizer',
    author='Sarvesh Chhabra',
    author_email='sarveshpoker@gmail.com',
    version='0.0.1',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)