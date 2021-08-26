import os

SRC = 'src/jenot/qt/__main__.py'
ICON = '--icon src/jenot/data/logo.ico'
NAME = '--name jenot-qt'
DATA = ' '.join(f"--add-data {src}{os.pathsep}{dst}" for src, dst in [
    ('src/jenot/data/*', 'jenot/data'),
    ('src/jenot/qt/ui/*', 'jenot/qt/ui'),
])


def task_pyinstaller():
    return {
        'actions': [
            'pyinstaller -y '
                f'{NAME} '
                f'{SRC} '
                f'{ICON} '
                f'{DATA} '
        ],
    }

def task_pyinstaller_of():
    return {
        'actions': [
            'pyinstaller -y '
                f'{NAME}-of '
                f'{SRC} '
                f'{ICON} '
                f'{DATA} '
                '--onefile '
        ],
    }
