from setuptools import setup

setup(
    name='hero_bot',
    version='1.0',
    description='Hero, the Discord bot!',
    author='Dreamsincs',
    packages=['hero_bot'],
    install_requires=['discord.py'],
    scripts=[
        './hero_bot'
    ]
)
