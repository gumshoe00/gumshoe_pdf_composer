from builtins import open

from setuptools import setup, find_packages


with open('README.md', 'r') as rfl:
    readme_content = rfl.read()


with open('LICENSE', 'r') as lfl:
    license_content = lfl.read()


setup(
    name='pdfcomposer',
    version='1.0.0',
    description='Composes one PDF from the given pdf files, in the given sequence.',
    url='https://github.com/gumshoe00/gumshoe_pdf_composer',
    long_description=readme_content,
    long_description_content_type='text/markdown',
    author='smikhail',
    author_email='gumshoe.media.inc@gmail.com',
    maintainer='Gumshoe Media Inc.',
    maintainer_email='gumshoe.media.inc@gmail.com',
    license=license_content,
    package_dir={'': 'src'},
    py_modules=find_packages("'src.pdfcomposer', 'src.pdfcomposer.*'"),
    install_requires=["setuptools", "importlib-metadata<5.0", "wheel"],
    python_requires='>=3.7',
    entry_points={
        "console_scripts": ["pdfcomposer=pdfcomposer.__main__:main",],
        "pdfcomposer.output": ["index=pdfcomposer.__main__:index",],
    },
    keywords=['PDF', 'composer', 'python3'],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
