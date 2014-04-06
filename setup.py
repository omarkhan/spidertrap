from distutils.core import setup

with open('README.rst') as readme:
    long_description = readme.read()

setup(
    name='spidertrap',
    version='0.1.1',
    description='Spider trap for testing crawlers',
    long_description=long_description,
    author='Omar Khan',
    author_email='omar@omarkhan.me',
    url='https://github.com/omarkhan/spidertrap',
    py_modules=['spidertrap'],
    scripts=['spidertrap'],
)
