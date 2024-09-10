from setuptools import setup, find_packages

setup(
    name='covid19_NYPD',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "plotly",
        "requests"
    ],

    author='Krzysiek Terlecki',
    author_email='kkterlecki@gmail.com',
    description='project for NYPD course, University of Warsaw Faculty of Mathematics, Informatics and Mechanics',
    python_requires='>=3.6',
)
