from distutils.core import setup

setup(
    name='Auth',
    version='0.1dev',
    packages=['footy_auth',],
    install_requires=['adal==1.2.1', 'azure-keyvault==1.1.0'],
    license='',
    long_description=open('README').read()
)
