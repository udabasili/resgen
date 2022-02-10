from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readline()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='respon_gen',
    version='1.0.0',
    author='Udendu Abasili',
    description='This package was made to help generate responsive images in bulk',
    url='https://github.com/udabasili/responsive-image-gen',
    email='udbasili@yahoo.com',
    long_description=long_description,
    license='MIT',
    packages=['respon_gen'],
    entry_points={
        'console_script': [
        ]
    },
    classifiers={
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Documentation',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    },
    keywords='responsive images python web development developer response_images_gen responsive images generator',
    install_requires=requirements,
    zip_safe=False
)
