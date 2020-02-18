import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="apple-orchard", # Replace with your own username
    version="0.0.0",
    author="Collette Anderson",
    author_email="frob@249517.no-reply.drupal.org",
    description="A program for playing Apple Orchard",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['pyobjc', 'arcade'],
    url="https://github.com/frob/orchard",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
