import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="makrl",
  version="0.0.1",
  author="Ryan Butler",
  author_email="thebutlah@gmail.com",
  description="Modular Algorithms Kit for Reinforcement Learning",
  long_description=long_description,
  # long_description_content_type="text/markdown",
  url="https://github.com/TheButlah/makrl",
  packages=setuptools.find_packages(),
  classifiers=(
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 2",
    "Intended Audience :: Science/Research",
    "Operating System :: OS Independent",
    "License :: Free for non-commercial use",
    "Topic :: Scientific/Engineering :: Artificial Intelligence",
    "Development Status :: 3 - Alpha",
  ),
  install_requires=[
    'six',
    'logzero',
    'gym',
    'atari-py',
    'keras',
  ],
)
