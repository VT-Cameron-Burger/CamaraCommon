"""Setup configuration for CAMARA Common Data Types package."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="camara-common-data-types",
    version="0.1.0",
    author="Cameron Burger",
    author_email="cameronburger@vt.edu",
    description="Pydantic models for CAMARA API common data types - Python implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VT-Cameron-Burger/camara-data-types",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Communications :: Telephony",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pydantic>=2.0.0,<3.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.21.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
        ],
        "test": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.21.0",
        ],
    },
    keywords="camara, api, pydantic, validation, telecommunications, 5g",
    project_urls={
        "Bug Reports": "https://github.com/VT-Cameron-Burger/camara-data-types/issues",
        "Source": "https://github.com/VT-Cameron-Burger/camara-data-types",
        "Documentation": "https://github.com/VT-Cameron-Burger/camara-data-types#readme",
        "CAMARA Project": "https://github.com/camaraproject",
        "CAMARA Specification": "https://github.com/camaraproject/Commonalities",
    },
)
