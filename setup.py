from setuptools import setup, find_packages
import pimm

setup(name='pimm',
      packages=['pimm'],
      version='0.0.2',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python', 'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9'
      ],
      install_requires=['ping3'],
      entry_points={'console_scripts': ['pmm=pimm.pimm_module:main']},
      package_data={'': ['*.json']},
      auth='lollipopnougat',
      author_email='lollipopnougat@126.com',
      description='pypi mirrors manager',
      long_description='a simple pypi mirrors manager, just like nrm for npm\n$ pmm ls # list all servers\n$ pmm test # show response time of all servers\n$ pmm use <server name> # use <server_name> server',
      url='https://github.com/lollipopnougat/pimm',
      license='MIT',
      keywords="pimm source manager")
