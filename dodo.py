def task_pyinstaller():
    return {
        'actions': [
            'rm -rf build dist ; '
            'pyinstaller \\'
                'src/jenot/qt/__main__.py \\'
                '--name jenot-qt-mf \\'
                '--icon src/jenot/data/logo.ico'
        ],
    }
