from builtins import open

from setuptools import setup, find_packages


with open('README.md', 'r') as rfl:
    readme_content = rfl.read()


with open('LICENSE', 'r') as lfl:
    license_content = lfl.read()


setup(
    name='gumshoe-pdf-composer',
    version='1.0.0',
    description='',
    long_description=readme_content,
    long_description_content_type='text/markdown',
    author='smikhail',
    author_email='gumshoe.media.inc@gmail.com',
    license=license_content,
    py_modules=['gumshoe_pdf_composer'],
    package_dir={'': 'src'},
    install_requires=["pikepdf", "python_version>='3.7'"],
    entry_points={"console_scripts": ["gumshoePdfCompose=src.gumshoe_pdf_compose:compose"]},
    keywords=['pdf', 'composer', 'python3+'],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
