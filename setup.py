from setuptools import setup

readme = ""
with open("README") as f:
    readme = f.read()

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
