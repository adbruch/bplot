from setuptools import setup

setup(name='bplot',
      version='0.1',
      description='Functional plotting.',
      url='http://github.com/roualdes/bplot',
      author='Edward A. Roualdes',
      author_email='eroualdes@csuchico.edu',
      license='BSD (3-clause)',
      install_requires=[
          'pandas',
          'matplotlib',
          'numpy',
          'scipy',
      ],
      packages=['bplot'],
      zip_safe=False)
