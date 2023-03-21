from setuptools import setup

setup(
    name="healthjoy-cc",
    version="1.0.0",
    packages=("healthjoy_cc",),
    install_requires=(
        "flask",
        "requests",
        "pytest",
    ),
)
