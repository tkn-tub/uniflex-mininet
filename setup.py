from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='uniflex_mininet',
    version='0.1.0',
    packages=find_packages(),
    url='https://github.com/uniflex',
    license='',
    author='Anatolij Zubow',
    author_email='{zubow}@tkn.tu-berlin.de',
    description='UniFlex Mininet',
    long_description='Running UniFlex agents in Mininet',
    keywords='wireless control mininet',
    install_requires=['pyyaml', 'docopt']
)
