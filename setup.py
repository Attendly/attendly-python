import os
from distutils.core import setup
from attendly import VERSION

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='Attendly',
    version=VERSION,
    author='Andrew Edwards',
    author_email='andrew@attendly.com',
    url='http://attendly.me/apidocs',
    packages=['attendly',],
    license='LICENSE.txt',
    long_description=open('README.rst').read(),
    install_requires=required,
    classifiers=[
        'Development Status :: Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: Apache 2 License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
