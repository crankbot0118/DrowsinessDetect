  
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DrowsinessDetect",
    version="0.0.1",
    author="Palepu Tarun Sathwik",
    author_email="palepu.tarun1801@gmail.com",
    description="nothing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ajayff4/DrowsinessDetect",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)