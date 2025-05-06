from setuptools import setup, find_packages

setup(
    name="painel_lili",
    version="1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "streamlit>=1.25.0",
        "pandas>=1.5.0",
        "python-docx>=0.8.11",
        "streamlit-js-eval>=0.1.5"
    ],
    author="Andrew Raimundo",
    description="Painel de Laudos Médicos com Reconhecimento de Voz via Streamlit",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)