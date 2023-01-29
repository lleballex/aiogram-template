i18n-extract:
	pybabel extract --input-dirs=src -o locales/messages.pot

i18n-compile:
	pybabel compile -d locales -D messages

i18n-update:
	pybabel update -d locales -D messages -i locales/messages.pot
