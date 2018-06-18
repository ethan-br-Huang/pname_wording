# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='pname_cut',
    version='0.0.0',
    license='BSD',
    description='',
    packages=['wording'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'jieba>=0.39',
        'regx'
    ],
    extras_require={
        'dev': [
            'pytest>=3',
        ],
    },
)
