from setuptools import setup
from os import path

import mupub

here = path.abspath(path.dirname(__file__))

setup(
    name = mupub.__title__,
    version = mupub.__version__,
    description = mupub.__summary__,
    url = mupub.__uri__,
    author = mupub.__author__,
    author_email = mupub.__author_email__,
    license = mupub.__license__,
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Topic :: Documentation :: Sphinx',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    packages = ['mupub', 'mupub.commands'],
    entry_points = {
        'mupub.registered_commands': [
            'init = mupub.commands.init:main',
            'check = mupub.commands.check:main',
            'tag = mupub.commands.tag:main',
            'build = mupub.commands.build:main',
            'clean = mupub.commands.clean:main',
        ],
        'console_scripts': [
            'mupub = mupub.__main__:main',
        ],
    },
    install_requires = [
        'pypng >= 0.0.18',
        'rdflib >= 4.2.1',
        'ruamel.yaml >= 0.12.18',
        'clint==0.5.1',
        'requests >= 2.11.1',
    ],
)
