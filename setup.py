from setuptools import setup, find_packages


setup(
    name='signalbot',
    version='0.0.1',
    url='https://signal-bot.github.io',
    license='AGPL-3.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'signal-bot=signalbot.cli:main',
        ]
    }
)
