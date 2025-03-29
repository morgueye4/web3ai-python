from setuptools import setup, find_packages

setup(
    name="web3ai",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "filecoin-storage",  # This will handle lighthouse and other providers
    ],
    author="gdaust",
    description="A modular Web3 AI Python library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/gdaust/web3ai-python",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
) 