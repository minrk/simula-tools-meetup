from setuptools import setup


setup(
    name="list_adder",
    description="Demo pre-commit hooks",
    version="1.0",
    author="Henrik Finsberg",
    license="MIT",
    author_email="henriknf@simula.no",
    url="https://github.com/minrk/simula-tools-meetup",
    packages=["list_adder"],
    install_requires=[
        "pytest",
        "numpy",
        "mypy",
        "flake8",
        "isort",
        "pre-commit",
        "black",
    ],
)
