from setuptools import setup, find_packages

setup(
    name="Enigma",
    version="0.1",
    description="An Enigma M3 simulation using python",
    url="https://github.com/Acelxrd95/Engima-Machine-Python",
    author="Yehia Mustafa Gouda",
    author_email="yehia.gouda@tkh.edu.eg",
    packages=find_packages(),
    entry_points={
        "console_scripts":["enigma=Enigma.cli:main"]
    },
    test_suite="tests",
)
