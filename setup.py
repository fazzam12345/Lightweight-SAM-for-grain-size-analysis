from setuptools import setup, find_packages

setup(
    name="paper-code-section",
    version="0.1.0",
    description="This code accompanies the publication 'Comparative Study of Segment Anything Models for Grain Size Analysis: One Step Towards Automation' and is provided for code availability and reproducibility.",
    packages=find_packages(include=["paper_code_section", "paper_code_section.*"]),
    python_requires=">=3.12",
)
