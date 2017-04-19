from setuptools import setup

setup(
    name='vortex',
    version='1.0',
    py_modules=['welcome'],
    install_requires=[
        'Click', 'requests'
    ],
    entry_points='''
        [console_scripts]
        hello=welcome:cli,
    ''',
)