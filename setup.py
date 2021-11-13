from setuptools import setup, find_packages

setup(
    name="Enigma",
    version="0.1",
    description="An Enigma M3 simulation using python",
    url="https://github.com/Acelxrd95/Engima-Machine-Python",
    author="Yehia Mustafa Gouda",
    author_email="yehia.gouda@tkh.edu.eg",
    packages=find_packages(),
    entry_points={"console_scripts": ["enigma=Enigma.cli:main"]},
    install_requires=[
        "click==8.0.3",
        "Faker>=9.8.0",
        "pycipher>=0.5.2",
        "regex==2021.11.2",
    ],
    test_suite="tests",
)
