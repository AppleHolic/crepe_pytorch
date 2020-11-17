import imp
import os
import pkg_resources
from setuptools import setup, find_packages


version = imp.load_source('crepe_pyorch.__version__', os.path.join('crepe_pyorch', '__version__.py'))


with open('README.md') as file:
    long_description = file.read()


setup(
    name='crepe_pyorch',
    version=version.version,
    description='Pytorch ported version of CREPE pitch tracker ',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Appleholic/crepe_pytorch',
    author='ILJI CHOI',
    author_email='choiilji@gmail.com',
    packages=find_packages(),
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Multimedia :: Sound/Audio :: Analysis',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='pitch',
    install_requires=[
        str(requirement)
        for requirement in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ]
)