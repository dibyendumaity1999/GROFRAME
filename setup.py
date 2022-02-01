import setuptools

#with open("README.md", "r", encoding="utf-8") as fh:
#    long_description = fh.read()
install_requires = []
with open("requirements.txt") as f:
    install_requires = f.read().splitlines()
#install_requires = open("requirements.txt").readlines()

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
    install_requires=install_requires,
)
