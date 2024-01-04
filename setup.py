from setuptools import setup, find_packages
import pimm
from pimm import pimm_const
from os import path
this_directory = path.abspath(path.dirname(__file__))
long_description = None

with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='pimm',
      packages=['pimm'],
      version=pimm_const.VERSION,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python', 'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: 3.11',
          'Programming Language :: Python :: 3.12'
      ],
      install_requires=['ping3'],
      entry_points={'console_scripts': ['pmm=pimm.pimm_module:main']},
      package_data={'': ['*.json']},
      auth='lollipopnougat',
      author_email='lollipopnougat@126.com',
      description='pypi mirrors manager',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/lollipopnougat/pimm',
      license='MIT',
      keywords="pimm source manager")
