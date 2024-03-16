from setuptools import setup
from setuptools import find_packages
setup(
    name='clockysap',
    version='0.7',
    packages=find_packages(),
    url='https://github.com/zudljk/clockysap',
    license='MIT',
    author='zudljk',
    author_email='zudljk@email.de',
    description='Import Clockify entries from the current month to SAP Successfactors',
    scripts=["clockysap"]
)
