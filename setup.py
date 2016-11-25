from setuptools import setup

setup(
    name='troposphere-helpers',
    version='0.0.1',
    description='Helper functions and classes for troposphere Templates',
    url='https://github.com/wearecloudar/troposphere-helpers',
    author='Ben Bridts',
    author_email='ben@cloudar.be',
    license='New BSD license',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='troposphere cloudformation aws',
    packages=['troposphere-helpers'],
    package_data={
        'troposphere-helpers': ['lambda_code/*.py'],
    },

    install_requires=['troposphere'],
)
