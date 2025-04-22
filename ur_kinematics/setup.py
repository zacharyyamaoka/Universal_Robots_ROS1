#!/usr/bin/env python

from setuptools import setup

package_name = 'ur_kinematics'

setup(
    name=package_name,
    version='1.4.0',
    packages=[package_name],
    package_dir={'': 'src'},
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='G.A. vd. Hoorn',
    maintainer_email='g.a.vanderhoorn@tudelft.nl',
    description='UR forward and inverse kinematics.',
    license='BSD',
)