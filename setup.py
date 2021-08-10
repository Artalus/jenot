import setuptools

setuptools.setup(
    name="jenot",
    version="0.0",
    packages=setuptools.find_packages(where='src'),
    package_dir={'': 'src'},
    license="MIT",
    python_requires=">=3.9",
    install_requires=[
        'requests',
        'ConfigArgParse',
        'py-notifier',
        'PyQt5',
        'PyQt5-stubs',
        'PyYAML',
    ],
    entry_points=dict(
        console_scripts=[
            'jenot = jenot.__main__:main',
            'jenotg = jenot.qt.__main__:main',
        ]
    ),
    package_data={'jenot': [
        'qt/ui/*.ui',
    ]}
)
