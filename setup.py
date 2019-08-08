from setuptools import setup

setup(
    name="bplot",
    version="0.2",
    description="Functional plotting.",
    url="http://github.com/roualdes/bplot",
    author="Edward A. Roualdes",
    author_email="eroualdes@csuchico.edu",
    license="BSD (3-clause)",
    install_requires=[
        "matplotlib>=3.0.0",
        "numpy>=1.7,<2.0",
        "scipy>=0.19.1",
        "pandas>=0.25.0",
    ],
    packages=["bplot"],
    package_dir={"": "src"},
    zip_safe=False,
)
