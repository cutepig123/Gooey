from distutils.core import setup

setup(
    name='Gooey',
    version='0.1.0',
    author='Chris Kiehl',
    author_email='ckiehl@gmail.com',
    packages=[
      'gooey',
      'gooey.gui',
      'gooey.images',
      'gooey.languages',
      'gooey.mockapplications',
    ],
    url='http://pypi.python.org/pypi/TowelStuff/',
    license='LICENSE.txt',
    description='Turn (almost) any command line program into a full GUI application with one line',
    long_description=open('README.md').read()
)