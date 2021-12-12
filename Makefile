build: main.py locales/
	msgfmt.py -o locales/en/LC_MESSAGES/base.mo locales/en/LC_MESSAGES/base
	msgfmt.py -o locales/tr/LC_MESSAGES/base.mo locales/tr/LC_MESSAGES/base