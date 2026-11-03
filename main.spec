# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all

block_cipher = None

enigma_datas, enigma_binaries, enigma_hiddenimports = collect_all('codeenigma_runtime')

a = Analysis(
    ['dist_obf/staging/gui.py'],
    pathex=['dist_obf/staging'],
    binaries=enigma_binaries,
    datas=enigma_datas,
    hiddenimports=enigma_hiddenimports + [
        'customtkinter', 'darkdetect',
        'json', 'sqlite3', 'datetime', 'uuid', 'hashlib', 'argparse',
        'os', 'sys', 'tkinter',
        'requests', 'cryptography',
        'cryptography.hazmat.primitives',
        'cryptography.hazmat.primitives.serialization',
        'cryptography.hazmat.primitives.asymmetric',
        'cryptography.hazmat.primitives.asymmetric.padding',
        'cryptography.hazmat.primitives.asymmetric.rsa',
        'cryptography.hazmat.primitives.hashes',
        'cryptography.hazmat.backends',
        'reportlab', 'reportlab.lib', 'reportlab.lib.pagesizes',
        'reportlab.lib.units', 'reportlab.lib.colors',
        'reportlab.lib.styles', 'reportlab.lib.enums',
        'reportlab.pdfgen', 'reportlab.pdfgen.canvas',
        'reportlab.platypus',
        'reportlab.pdfbase', 'reportlab.pdfbase.pdfmetrics',
        'reportlab.pdfbase.ttfonts',
        'main', 'report_generator', 'database', 'documents',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz, a.scripts, a.binaries, a.zipfiles, a.datas,
    [], name='main', debug=False, bootloader_ignore_signals=False,
    strip=False, upx=True, upx_exclude=[], runtime_tmpdir=None, console=False,
)
