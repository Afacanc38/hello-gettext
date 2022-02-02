update-locales: msgfmt.py main.py locales/
	python3 msgfmt.py -o locales/en/LC_MESSAGES/base.mo locales/en/LC_MESSAGES/base
	python3 msgfmt.py -o locales/tr/LC_MESSAGES/base.mo locales/tr/LC_MESSAGES/base

locale: pygettext.py main.py locales/
	python3 pygettext.py -d base -o locales/base.pot main.py
	cp locales/base.pot locales/tr/LC_MESSAGES/base.po
	cp locales/base.pot locales/en/LC_MESSAGES/base.po
