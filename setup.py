import setuptools

setuptools.setup(
    include_package_data=True,
    name='portscan',
    version='0.0.1',
    description='Program for scanning ports bassed on nmap',
    url='https://github.com/bender321/ScanPort',
    author='bender321',
    contact='example@example.com',
    packages=setuptools.find_packages(),
    install_requires=['nmap'],
    long_description='Program for scanning ports bassed on nmap',
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)


