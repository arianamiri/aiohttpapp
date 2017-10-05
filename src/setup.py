from setuptools import setup, find_packages

setup(
    name='Concierge',
    version='0.0.1',
    packages=find_packages(),
    install_requires=('aiohttp==2.2.5',)
)
