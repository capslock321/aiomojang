import setuptools

setuptools.setup(
    name="aiomojang",
    version="0.5",
    author="capslock321",
    description="An asynchronous Python wrapper for Mojang's API",
    url="https://github.com/capslock321/aiomojang/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
