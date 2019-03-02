import os, setuptools


def parse_requirements():
    with open("requirements.txt") as f:
        return [l.strip('\n') for l in f if l.strip('\n') and not l.startswith('#') and not l.startswith("-")]

additional_kwargs = {}
if os.path.exists("requirements.txt"):
    additional_kwargs.update({
        "install_requires": parse_requirements()
    }) 

setuptools.setup(
    name='{{ cookiecutter.pkg_name }}',
    version='0.1',
    packages=setuptools.find_packages(exclude=["tests*"]), # include all packages under this package
    **additional_kwargs
)