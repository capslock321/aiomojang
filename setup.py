import setuptools

setuptools.setup(
    name="aiomojang",
    version="0.3",
    author="capslock321",
    description="An asynchronous python wrapper of Mojangs API",
    url="https://github.com/capslock321/aiomojang/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
