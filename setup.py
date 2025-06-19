from setuptools import setup, find_packages
import os

# Ler o README para a descrição longa
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return ""

# Ler os requisitos
def read_requirements():
    req_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    if os.path.exists(req_path):
        with open(req_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return []

setup(
    name="cloudvbox-dark-theme",
    version="1.0.3",
    author="cloudvBOX Team",
    author_email="contato@cloudvbox.com",
    description="Tema profissional escuro para Jupyter Notebook e JupyterLab com identidade visual cloudvBOX",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/cloudvbox/cloudvbox-dark-theme",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: User Interfaces",
        "Framework :: Jupyter",
    ],
    python_requires=">=3.7",
    install_requires=read_requirements(),
    include_package_data=True,
    package_data={
        "cloudvbox_dark_theme": [
            "static/css/*.css",
            "static/js/*.js", 
            "static/images/*",
            "templates/*",
        ],    },
    entry_points={
        "console_scripts": [
            "cloudvbox-theme-install=cloudvbox_dark_theme.install:install_theme",
            "cloudvbox-theme-uninstall=cloudvbox_dark_theme.install:uninstall_theme",
            "cloudvbox-theme=cloudvbox_dark_theme.cli:main",
        ],
    },
    keywords="jupyter notebook jupyterlab theme dark cloudvbox",
    project_urls={
        "Bug Reports": "https://github.com/cloudvbox/cloudvbox-dark-theme/issues",
        "Source": "https://github.com/cloudvbox/cloudvbox-dark-theme",
        "Documentation": "https://github.com/cloudvbox/cloudvbox-dark-theme#readme",
    },
)

