from setuptools import setup, find_packages

setup(
    name='user_greeting',
    version='0.1',
    description='This project is an application that greets users and stores their data in persistent storage.',
    author='Duvan Andrés Amado',
    packages=find_packages(where='src'), 
    package_dir={'': 'src'}, 
    install_requires=[
        'Flask>=2.0.0',
        'mysqlclient',
        'flask_mysqldb',
        'pytest'
    ],
    entry_points={
        'console_scripts': [
            'user_greeting=app.main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
