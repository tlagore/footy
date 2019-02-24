from distutils.core import setup

setup(
    name='Auth',
    version='0.1dev',
    packages=['auth',],
    install_requires=['adal==1.2.1'],
    license='',
    long_description=open('README').read()
)
