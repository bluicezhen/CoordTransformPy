from distutils.core import setup

setup(
    name='MapDatumTrans',
    packages=['map_datum_trans'],  # Chose the same as "name"
    version='0.0.1',
    license='MIT',
    description='A Transformer for different map datum, include WGS84, GCJ-02, BD-09',
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
