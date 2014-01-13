from setuptools import setup, find_packages
import os

version = '0.1'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
+ '\n')

setup(
    name = 'collective.googleauthenticator',
    version = version,
    description = "Two-step verification for Plone 4 using the Google Authenticator app.",
    long_description = long_description,
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers = [
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords = 'google authenticator, two-step verification, multi-factor authentication, two-factor authentication',
    author = 'Goldmund, Wyldebeast & Wunderliebe',
    author_email = 'info@gw20e.com',
    url = 'https://github.com/collective/collective.googleauthenticator',
    license = 'GPL 2.0',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    namespace_packages = ['collective', ],
    include_package_data = True,
    zip_safe = False,
    install_requires = [
        'setuptools',
        # -*- Extra requirements: -*-
        'plone.api==1.1.0',
        'plone.directives.form>=1.1',
        'onetimepass==0.2.2',
        'ska==1.1',
        'rebus==0.1',
    ],
    extras_require = {'test': ['plone.app.testing', 'robotsuite']},
    entry_points = """
        # -*- Entry points: -*-
        [z3c.autoinclude.plugin]
        target = plone
    """,
)