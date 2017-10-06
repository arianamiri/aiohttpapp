from setuptools import setup, find_packages

setup(
    name='Concierge',
    version='0.0.1',
    packages=find_packages(),
    install_requires=(
        'aiohttp==2.2.5',
        'psycopg2==2.7.3.1',
        'SQLAlchemy==1.1.14',
    )
)
