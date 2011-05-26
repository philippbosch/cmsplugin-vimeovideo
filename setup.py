from setuptools import setup, find_packages

VERSION = __import__("cmsplugin_vimeovideo").__version__

setup(
    name='cmsplugin-vimeovideo',
    version=VERSION,
    description='Vimeo video plugin for django-cms',
    long_description=open('README').read(),
    author='Philipp Bosch',
    author_email='hello@pb.io',
    maintainer='Philipp Bosch',
    maintainer_email='hello@pb.io',
    url='http://github.com/philippbosch/cmsplugin-vimeovideo',
    license='BSD',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[]
)
