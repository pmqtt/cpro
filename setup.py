from setuptools import setup



setup(
    name='cpro',
    version='0.5.1',
    packages=['cpro'],
    url='',
    license='Apache 2',
    author='michael burzan',
    author_email='',
    description='',
    install_requires = ['watchdog==0.10.3'],
    entry_points={
        'console_scripts': [
            'cpro=cpro:run',
        ],
    }
)
