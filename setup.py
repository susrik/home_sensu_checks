from setuptools import setup, find_packages

setup(
    name='home-sensu-checks',
    version="0.01",
    author='Erik Reid',
    author_email='merikreid@gmail.com',
    description='Custom checks/metrics for use with Sensu',
    url=('https://github.com'),
    packages=find_packages(),
    install_requires=[
        'click',
        'fritzconnection',
    ],
    entry_points = {
        'console_scripts': [
            'fritz-metrics=home_sensu_checks.fritz:cli',
        ]
    }
)
