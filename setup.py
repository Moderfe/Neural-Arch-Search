from setuptools import setup, find_packages

setup(
    name=\'neural_arch_search\',
    version=\'0.1.0\',
    packages=find_packages(where=\'src\'),
    package_dir={\'\': \'src\'},
    install_requires=[
        \'numpy>=1.18.0\',
    ],
    author=\'Marcus D. Sterling\',
    author_email=\'erarealorgrun@gmx.net\',
    description=\'A framework for Neural Architecture Search (NAS) to discover optimal neural network designs.\',
    long_description=open(\'README.md\').read(),
    long_description_content_type=\'text/markdown\',
    url=\'https://github.com/Moderfe/Neural-Arch-Search\',
    classifiers=[
        \'Programming Language :: Python :: 3\',
        \'License :: OSI Approved :: MIT License\',
        \'Operating System :: OS Independent\',
        \'Intended Audience :: Developers\',
        \'Intended Audience :: Science/Research\',
        \'Topic :: Scientific/Engineering :: Artificial Intelligence\',
    ],
    python_requires=\'>=3.8\',
)
