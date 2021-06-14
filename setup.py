from setuptools import setup

readme = ""
with open("README.md") as f:
    readme = f.read()

setup(
    name="pycamera",
    version="0.2.1",
    description="An easier solution to computer vision.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/IsmaeelAkram/pycamera",
    author="Ismaeel Akram",
    python_requires=">=3.4.0",
    license="MIT",
    install_requires=["opencv-python", "numpy"],
    packages=["pycamera"],
    zip_safe=False,
)
