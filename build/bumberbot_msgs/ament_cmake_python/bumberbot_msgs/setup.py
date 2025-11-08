from setuptools import find_packages
from setuptools import setup

setup(
    name='bumberbot_msgs',
    version='0.0.0',
    packages=find_packages(
        include=('bumberbot_msgs', 'bumberbot_msgs.*')),
)
