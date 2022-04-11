import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="shitsort",
    version="1.1.1",
    description="Really really bad sorting algorithms",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/sh6heer/shitty-sorting-algorithms",
    author="sh6heer",
    author_email="",
    license="GNU GPLv3",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["shitsort"],
    include_package_data=True,
    # install_requires=["multiprocessing"],
    # entry_points={
    #     "console_scripts": [
    #         "realpython=reader.__main__:main",
    #     ]
    # },
)
