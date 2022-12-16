from setuptools import setup, find_packages


def requirements(file_name):
    return open(file_name, 'rt').read().splitlines()


setup(
    name='',
    url='',
    author='',
    description='',
    author_email='',
    version='0.0.1',
    packages=find_packages(),
    install_requires=requirements('requirements.txt'),
)
