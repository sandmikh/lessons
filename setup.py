from setuptools import setup, find_packages

from os.path import join, dirname

import helloMisha

setup(
    name='hi',
    version=helloMisha.__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    include_package_data=True,
    install_requires=[
            'Flask==0.8'
        ],

    entry_points={
        'console_scripts':
            ['hi = helloMisha.core:print_message',
            'serve = helloMisha.web:run_server',
            ]
    },
    test_suite='tests'


)