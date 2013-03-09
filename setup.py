from setuptools import setup, find_packages

setup(
    name='python2-http-wrapper',
    version='0.0.1',
    description='Very basic HTTP wrapper for python2',
    long_description=open('README.md').read(),
    author='Daniel Perez',
    author_email='tuvistavie@gmail',
    url='https://github.com/tuvistavie/python2-http-wrapper',
    download_url='https://github.com/tuvistavie/python2-http-wrapper/archive/master.zip',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: MIT',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP'
    ],
)
