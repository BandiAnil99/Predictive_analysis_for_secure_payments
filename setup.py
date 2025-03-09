from setuptools import setup, find_packages

setup(
    name="MyFlaskApp",
    version="1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "flask",
        "mysql-connector-python",
        "pandas",
        "numpy",
        "scikit-learn",
        "joblib"
    ]
)
