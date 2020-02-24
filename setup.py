from setuptools import setup

with open('README.md') as f:
    readme = f.read()

setup(
    name="ttt",
    version="0.0.1",
    packages=['ttt'],
    description='Togai Tsv Tool',
    long_description=readme,
    url='https://github.com/garicchi/ttt',
    author='garicchi',
    author_email='xgaricchi@gmail.com',
    python_requires='>=3.6',
    license='MIT',
    scripts=['ttt']
)
