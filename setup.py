import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")


setup(
    name="pyedgeconnect",
    use_scm_version={
        "local_scheme": "no-local-version",
        "write_to": "_version.py",
        "write_to_template": 'version = "{version}"\n',
    },
    setup_requires=["setuptools_scm"],
    description="A Python wrapper for Aruba Orchestrator and Edge Connect API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SPOpenSource/edgeconnect-python",
    author="Zach Camara",
    author_email="zachary.camara@hpe.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Telecommunications Industry",
        "Topic :: System :: Networking",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ],
    keywords="silver peak, silverpeak, silver peak python, aruba edge connect, edge connect",
    packages=find_packages(),
    package_dir={"pyedgeconnect": "pyedgeconnect"},
    python_requires=">=3.9, <4",
    zip_safe=False,
    install_requires=["requests"],
    extras_require={
        "dev": [
            "black",
            "flake8",
            "flake8-rst-docstrings",
            "isort",
            "sphinx",
            "sphinx_rtd_theme",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/SPOpenSource/edgeconnect-python/issues",
        "Source": "https://github.com/SPOpenSource/edgeconnect-python/",
    },
)
