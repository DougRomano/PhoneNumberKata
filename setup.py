try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'PhoneNumberKata',
	'author': 'Doug Romano',
	'url': 'URL to get it at',
	'download': 'Where to download it',
	'author_email': 'doug.c.romano@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['PhoneNumber'],
	'scripts': [],
	'name': 'PhoneNumberKata'
}

setup(**config)