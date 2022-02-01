import setuptools

#with open("README.md", "r", encoding="utf-8") as fh:
#    long_description = fh.read()

setuptools.setup(
    name='GROFRAME',
    version='0.0.1',
    author='Dibyendu Maity',
    author_email='dibyendumaity1999@bose.res.in',
    description='Testing installation of Package',
    #long_description=long_description,
    #long_description_content_type="text/markdown",
    url='https://github.com/dibyendumaity1999/GROFRAME',
    project_urls = {
        "Bug Tracker": "https://github.com/dibyendumaity1999/GROFRAME/issues"
    },
    license='MIT',
    packages=['GROFRAME'],
    install_requires=['requests'],
)