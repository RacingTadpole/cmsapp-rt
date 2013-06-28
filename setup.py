import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = 'cmsapp-rt',
    version = '0.0.4',
    packages = find_packages(),   
    include_package_data = True,
    license = 'BSD License', 
    description = 'This package contains one app (including a context processor and example template) to help your Django-CMS project work with Twitter Bootstrap',
    long_description = README,
    keywords = "globals bootstrap racing tadpole",
    url = 'https://github.com/RacingTadpole/cmsapp-rt',
    author = 'Art Street',
    author_email = 'art@racingtadpole.com',
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    zip_safe = False,
    install_requires = [
        'django-singleton-admin',
    ],
)
