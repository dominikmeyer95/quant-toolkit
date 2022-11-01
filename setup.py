from setuptools import setup, find_packages

setup(
    name="quant_toolkit",
    version='0.1.0',
    author="Dominik Meyer",
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.10',
    install_requires=[
        'numpy=>1.23.4'
        'pandas=>1.5.1'
        'scipy=>1.9.3'
        'statsmodels=>0.13.2'
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent'
    ],

)
