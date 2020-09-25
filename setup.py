from setuptools import setup

setup(
    name='MapDatumTrans',
    packages=['MapDatumTrans'],
    version='1.0.0',
    license='MIT',
    description='A Transformer for different map datum, include WGS84, GCJ-02, BD-09',
    long_description_content_type='text/markdown',
    long_description=open("README.md", "r", encoding='utf-8').read(),
    author='Bluice Zhen',
    author_email='bluice.zhen@gmail.com',
    url='https://github.com/bluicezhen/MapDatumTrans',
    keywords=['WGS84', 'GCJ-02', 'BD-09'],
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],

)
