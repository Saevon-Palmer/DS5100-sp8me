from setuptools import setup, find_packages

setup(
    name = "montecarlo",
    version = "1.0.0",
    packages = find_packages(),
    install_requires = [
        "numpy",
        "pandas",
    ],
    author = "Sae'von Palmer",
    author_email = "palmersaevon@gmail.com",
    license = "MIT",
    description = "A Monte Carlo Simulator for Final Project",
    url = "https://github.com/Saevon-Palmer/DS5100-sp8me/Final%20%Project",
)