from pathlib import Path

import PyInstaller.__main__

name = "pg_creds"
path_to_main = "./main.py"


def install():
    PyInstaller.__main__.run([
        path_to_main,
        '--onefile',
        '--windowed',
        '--name',
        name,
        '--paths',
        '.'
    ])


if __name__ == '__main__':
    install()
