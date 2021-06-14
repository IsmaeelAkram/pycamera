from setuptools import setup

setup(
    name="pycamera",
    version="0.2",
    description="An easier solution to computer vision.",
    url="https://github.com/IsmaeelAkram/pycamera",
    author="Ismaeel Akram",
    license="MIT",
    install_requires=["opencv-python", "numpy"],
    packages=["pycamera"],
    zip_safe=False,
)
