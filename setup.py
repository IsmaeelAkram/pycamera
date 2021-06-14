from setuptools import setup

setup(
    name="pycamera",
    version="0.1",
    description="An easier solution to simple computer vision",
    url="https://github.com/IsmaeelAkram/pycamera",
    author="Ismaeel Akram",
    license="MIT",
    install_requires=["opencv-python", "numpy"],
    packages=["pycamera"],
    zip_safe=False,
)
