import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext
from setuptools import setup, find_packages


def read_file(fname):
    "Read a local file"
    return open(join(dirname(__file__), fname)).read()


setup(
    name='mkdocs-codeinclude-plugin',
    version='0.0.1',
    description="A plugin for mkdocs that allows some advanced 'includes' functionality to be used for embedded code blocks.",
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    keywords='mkdocs python markdown codeinclude',
    url='https://github.com/rnorth/mkdocs-codeinclude-plugin',
    author='Richard North',
    author_email='TODO',
    python_requires='>=3.6',
    install_requires=[
        'mkdocs>=0.17',
        'mkdocs'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
    ],
    packages=['codeinclude'],
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    entry_points={
        'mkdocs.plugins': [
            'codeinclude = codeinclude.plugin:CodeIncludePlugin'
        ]
    },
    test_suite="nose.collector",
    tests_require=["nose"]
)