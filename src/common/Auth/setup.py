# below line disables an error in pylint where it can't find a module 
# that exists in a virtual environment
from distutils.core import setup # pylint: disable=no-name-in-module,import-error

setup(
    name='Auth',
    version='0.1dev',
    packages=['auth',],
    license=''
)