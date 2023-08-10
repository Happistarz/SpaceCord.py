from setuptools import setup, find_packages

setup(
    name="SpaceCord.py",
    version="0.0.1",
    author="happiz",
    author_email="",
    description="A discord bot framework",
    long_description="",
    long_description_content_type="text/markdown",
    url="",  # TODO
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.8",
    install_requires=["discord.py"],
)
