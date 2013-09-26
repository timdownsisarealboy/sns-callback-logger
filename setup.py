from setuptools import setup
import os
import distutils.sysconfig
pre = distutils.sysconfig.get_config_var("prefix")
bindir = os.path.join(pre, "bin/activate")

setup(
    name='sns-callback',
    version='0.0.1',
    description='sns callbacks',
    author='Tim Downs',
    author_email='tim@framestack.com',
    zip_safe=False,
    include_package_data=True,
    url='http://framestack.com',
    platforms=["any"],
    dependency_links=[],
    install_requires=[
        'flask',
    ]
)
