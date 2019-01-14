try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'BSTree.',
    'author': 'Murphian',
    'url': 'XXXXXXXXXX',
    'download_url': 'XXXXXXXXXXXXX',
    'author_email': 'murphianx@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex20'],
    'scripts': [],
    'name': 'ex20'
}

setup(**config)