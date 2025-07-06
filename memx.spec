# -*- mode: python ; coding: utf-8 -*-
block_cipher = None
a = Analysis(
    ["main.py"],
    pathex=["."],
    binaries=[("EmptyStandbyList.exe", ".")],
    datas=[
        ("memx.ico", "."),
        ("memx.png", "."),
        ("information.png", "."),
    ],
    hiddenimports=[
        "customtkinter",
        "CTkToolTip",
        "win32timezone",   # يتطلبه pywin32
    ],
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name="MemX",
    icon="memx.ico",
    debug=False,
    strip=False,
    upx=True,
    console=False,   # نمنع ظهور نافذة الـ CMD
)
