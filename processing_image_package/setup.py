from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup (
    name="package_name",
    version="0.0.1",
    author="Bruno Alves"
    author_email="brunobrdk@outllo.com"
    description="pacote de processamento de imagens",
    long_description= page_description,
    long_description_content_type= ""
    url="https://github.com/brunobrd/processing_image",
    packages=find_packages(),
    install_requieres= requirements
    python_requires= >3.3
)
