from setuptools import setup
import os
from glob import glob

package_name = 'inspection_bot_nav'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
    ],
    install_requires=['setuptools', 'pyyaml'],
    zip_safe=True,
    maintainer='Ashraf',
    maintainer_email='ashraf@example.com',
    description='Planification TSP de la tournée d\'inspection + commander Nav2',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'tsp_planner = inspection_bot_nav.tsp_planner:main',
            'inspection_commander = inspection_bot_nav.inspection_commander:main',
        ],
    },
)
