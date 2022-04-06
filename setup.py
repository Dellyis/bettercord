import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bettercord",
    version="1.0.0",
    author="Dellyis",
    author_email="pypi@dellyis.me",
    description="An async wrapper for BetterCord API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Dellyis/bettercord",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">= 3.8",
)