from setuptools import setup,find_packages

print (find_packages)

with open('requirements.txt', 'r', encoding='utf-8') as f:
    requirements = f.read().split('\n')

setup(
    name='mypackage',
    version='0.0.1',
    install_requires=requirements,
    
   
)

