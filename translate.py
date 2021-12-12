try:
    import getdtext, os
except:
    print("\a\033[1;91merror\033[0;1m: Gettext (localization module) not found.")
    print("\a\033[1;96minfo\033[0;1m: Exit code: 1")
    exit(1)

envkey = 'LANG'
lang = os.getenv(key)
if 'tr' in lang:
    tr = gettext.translation('base', localedir='locales', languages=['tr'])
    tr.install()
    _ = tr.gettext
else:
    en = gettext.translation('base', localedir='locales', languages=['en'])
    en.install()
    _ = en.gettext
os.system("rm -rf __pycache__")