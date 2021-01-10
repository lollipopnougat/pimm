from setuptools import setup, find_packages
import pmm

setup(
    name='pmm',
    packages=['pmm'],
    version='0.0.3',
    classifiers=['Development Status :: 3 - Alpha'],
    install_requires=['ping3'],
    entry_points={  # 设置了在命令行中如何使用 greeting_module  中的 main 函数
        'console_scripts': ['pmm=pmm.pmm_module:main']
    },
    package_data={'': ['*.json']},
    auth='lollipopnougat',
    author_email='lollipopnougat@126.com',
    description='pypi mirrors manager',
    long_description='a simple pypi mirrors manager, just like nrm for npm',
    url='https://github.com/lollipopnougat/pmm',
    license='MIT',
    keywords="pmm manager")
