
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='mp-search',
    version='1.0.0',
    description='Improved Django search',
    long_description=open('README.md').read(),
    author='Paul Maigutyak',
    author_email='pmaigutyak@gmail.com',
    url='https://github.com/pmaigutyak/mp-search',
    packages=['search'],
    license='MIT'
)
