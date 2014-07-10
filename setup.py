from setuptools import setup

setup(
    name='PyAltmetric',
    version='0.1.0',
    author='Lauren Revere',
    author_email='lauren.revere@gmail.com',
    packages=['pyaltmetric'],
    url='http://pypi.python.org/pypi/PyAltmetric/',
    license='LICENSE.txt',
    description='A python wrapper for the Altmetric API.',
    long_description=open('README.txt').read(),
    install_requires=['requests==2.3.0'],
)
