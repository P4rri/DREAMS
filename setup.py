from setuptools import setup, find_packages

setup(
    name="dreamsecho",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'streamlit>=1.29.0',
        'pandas>=2.0.0',
        'numpy>=1.24.0',
    ],
    author="Votre Nom",
    author_email="votre.email@example.com",
    description="Une application de journal de rêves avec analyse",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/votrecompte/dreamsecho",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
