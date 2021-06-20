from setuptools import setup

with open('pypi_desc.md') as f:
    long_description = f.read()

setup(
    name='scratch_gpio_extend',
    version='0.1',
    packages=[
      'scratch_gpio_extend',
      'scratch_gpio_extend.gateways'
    ],
    install_requires=[
        'python-banyan>=3.9',
        'pymata-express>=1.11',
        'pymata_rh',
        'pymata-cpx',
        'tmx-pico-aio',
        'telemetrix-aio'
    ],

    entry_points={
        'console_scripts': [
            's3a = scratch_gpio_extend.s3a:s3ax',
            's3c = scratch_gpio_extend.s3c:s3cx',
            's3e = scratch_gpio_extend.s3e:s3ex',
            's3p = scratch_gpio_extend.s3p:s3px',
            's3r = scratch_gpio_extend.s3r:s3rx',
            's3rh = scratch_gpio_extend.s3rh:s3rhx',
            's3rp = scratch_gpio_extend.s3rp:s3rpx',
            'ardgw = scratch_gpio_extend.gateways.arduino_gateway:arduino_gateway',
            'cpxgw = scratch_gpio_extend.gateways.cpx_gateway:cpx_gateway',
            'espgw = scratch_gpio_extend.gateways.esp8266_gateway:esp8266_gateway',
            'pbgw = scratch_gpio_extend.gateways.picoboard_gateway:picoboard_gateway',
            'rpigw = scratch_gpio_extend.gateways.rpi_gateway:rpi_gateway',
            'rhgw = scratch_gpio_extend.gateways.robohat_gateway:robohat_gateway',
            'rpgw = scratch_gpio_extend.gateways.rpi_pico_gateway:rpi_pico_gateway',
            'wsgw = scratch_gpio_extend.gateways.ws_gateway:ws_gateway',
        ]
    },

    url='https://github.com/barkhaneum/scratch_gpio_dev',
    license='GNU Affero General Public License v3 or later (AGPLv3+)',
    author='BarkHaneum',
    author_email='majingazzz@naver.com',
    description='scratch3 gpio test',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['Scratch3', 'Arduino', 'ESP-8266', 'Raspberry Pi'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Other Environment',
        'Intended Audience :: Education',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Topic :: Education',
        'Topic :: Software Development',
        'Topic :: System :: Hardware'
    ],
)
