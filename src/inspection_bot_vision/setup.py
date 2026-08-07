from setuptools import setup

package_name = 'inspection_bot_vision'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'opencv-python', 'numpy', 'paho-mqtt'],
    zip_safe=True,
    maintainer='Ashraf',
    maintainer_email='ashraf@example.com',
    description='Détection d\'anomalies visuelles + publication ROS2/MQTT',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'anomaly_detector = inspection_bot_vision.anomaly_detector:main',
        ],
    },
)
