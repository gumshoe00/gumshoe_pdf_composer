from builtins import open

from setuptools import setup, find_packages


with open('README.md', 'r') as rfl:
    readme_content = rfl.read()


with open('LICENSE', 'r') as lfl:
    license_content = lfl.read()


setup(
    name='pdf-composer',
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
    py_modules=find_packages('pdf_composer'),

    install_requires=["setuptools", "importlib-metadata<5.0", "wheel"],
    python_requires='>=3.7',
    entry_points={
        "console_scripts": ["pdf-composer=pdf_composer.__main__:main",],
        "pdf_composer.output": ["default=pdf_composer.__main__:default",],
    },
    keywords=['PDF', 'composer', 'python3'],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
