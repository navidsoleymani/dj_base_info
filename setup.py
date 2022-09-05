from setuptools import setup, find_packages

setup(
    name='dj_base_info',
    version='0.01',
    license='MIT',
    author='nvd',
    author_email='navidsoleymani@ymail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/beensi-packages/responses.git',
    keywords='django base information models',
    install_requires=[
    ],
)
