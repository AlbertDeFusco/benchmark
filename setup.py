from setuptools import find_packages, setup

setup(
    name="torchbench",
    version="0.1",
    description="Benchmarking library for PyTorch",
    author="PyTorch Team",
    url="https://github.com/pytorch/benchmark",
    packages=find_packages(include=["torchbenchmark*", "userbenchmark*"]),
    include_package_data=True,
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: BSD 3 License",
        "Programming Language :: Python",
    ],
)
