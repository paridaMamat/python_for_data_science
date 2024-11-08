from setuptools import setup, find_packages

setup(
    name='ft_package',
    version='0.0.1',
    description='A sample test package',
    author='eagle',
    author_email='eagle@42.fr',
    license='MIT',  # Corrected 'License' to 'license'
    url='https://github.com/eagle/ft_package',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)
