from setuptools import setup, find_packages, dist
import os

# Ensure build dependencies are available before importing numpy and cythonize
dist.Distribution().fetch_build_eggs(['Cython>=0.29,<1.0', 'numpy>=1.19,<2.0'])

import numpy as np
from Cython.Build import cythonize

# Define required packages and extras
required = [
    "pytest",
    "cython>=0.29,<1.0",
    "numpy>=1.19,<2.0",
    "tensorflow==1.14",
    "numba==0.53.1",
    "sympy",
    "pandas==0.22",
    "scikit-learn",
    "click",
    "deap",
    "pathos",
    "seaborn",
    "progress",
    "tqdm",
    "commentjson",
    "PyYAML",
    "prettytable"
]

extras = {
    "control": [
        "mpi4py",
        "gym[box2d]==0.15.4",
        "pybullet",
        "stable-baselines[mpi]==2.10.0"
    ],
    "regression": []
}
extras['all'] = list(set([item for group in extras.values() for item in group]))

setup(
    name='dso',
    version='1.0.dev0',  # 规范化版本号
    description='Deep symbolic optimization.',
    author='LLNL',
    packages=find_packages(),  # 自动发现所有包和子包
    ext_modules=cythonize(
        [os.path.join('dso', 'cyfunc.pyx')],
        compiler_directives={'language_level': 3}  # 设置Cython语言级别
    ),
    include_dirs=[np.get_include()],
    install_requires=required,
    extras_require=extras,
)
