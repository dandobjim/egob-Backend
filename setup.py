from os.path import abspath, dirname, join

from setuptools import find_packages, setup

basedir = abspath(dirname(__file__))

with open(join(basedir, "README.md"), encoding="utf-8") as f:
    README = f.read()

with open(join(basedir, "egob", "__init__.py"), "r") as f:
    version_marker = "__version__ = "
    for line in f:
        if line.startswith(version_marker):
            _, VERSION = line.split(version_marker)
            VERSION = VERSION.strip().strip('"')
            break
    else:
        raise RuntimeError("Version not found on __init__")

install_requires = [
    # routes
    "fastapi",
    "pydantic[dotenv]",
    "uvicorn",
    "aiofiles",
    "pyjwt",
    "passlib[bcrypt]",
    "python-multipart",
    "strconv",
    "requests",
    
    #package
    "SPARQLWrapper",
]

setup(
    name="egob",
    version=VERSION,
    description="E-Goberment",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Khaos Research",
    author_email="",
    maintainer="Daniel Doblas",
    maintainer_email="",
    license="MIT",
    url="",
    packages=find_packages(exclude=["test_"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
    ],
    entry_points={"console_scripts": ["egob=egob.__main__:cli",],},
    install_requires=install_requires,
)
