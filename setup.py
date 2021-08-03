import setuptools

setuptools.setup(
    name="jenot",
    version="0.0",
    packages=setuptools.find_packages(where='src'),
    package_dir={'': 'src'},
    license="MIT",
    python_requires=">=3.6",
    install_requires=[
        'requests',
        'ConfigArgParse',
        'py-notifier',
    ],
    entry_points=dict(
        console_scripts=[
            'jenot = jenot.__main__:main'
        ]
    )
)
