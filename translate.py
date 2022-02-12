try:
    import gettext, os
except:
    print("\a\033[1;91merror\033[0;1m: Gettext (localization module) not found.")
    print("\a\033[1;96minfo\033[0;1m: Exit code: 1\033[0m")
    exit(1)
for lang in ['tr', 'en']:
    lang_translations = gettext.translation('base', localedir='locales', languages=[lang], fallback=True)
    lang_translations.install()
    _ = lang_translations.gettext

os.system("rm -rf __pycache__")
