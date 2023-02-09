# ⚡ Aiogram bot template

It is a template you can use for creating telegram bot with aiogram 3. It supports internationalization

### Tools:

- 💪 Aiogram (v3)
- 😄 i18n
- 🤹🏽 Loguru

## 🔥 Getting started

### Requirements:

- Python
- Make

### Installing

###### For linux

```bash
git clone git@github.com:lleballex/aiogram-template.git
cd aiogram-template
python3 -m venv env
. env/bin/activate
pip install -r requirements.txt
```

###### For windows

```bash
git clone git@github.com:lleballex/aiogram-template.git
cd aiogram-template
python -m venv env
env\scripts\activate
pip install -r requirements.txt
```

### Starting

```bash
python src/bot.py
```

## ✍ Adding handlers

Just create new file in *src/handlers* folder or its subfolder

#### Initialize router and use it to handle events:

```python
from aiogram import Router
my_router = Router()
```

#### Add created router to router list in *src/handlers/\_\_init\_\_.py*:

```python
from .my_file import my_router
routers = [my_router]
```

## 📖 Internationalization

This template uses i18n. So wrap your messages in `aiogram.utils.i18n.gettext` to make it translatable\
More information you can find [here](https://docs.aiogram.dev/en/dev-3.x/utils/i18n.html#step-3-translate-texts)

#### Extracting messages (creating .pot):

```bash
make i18n-extract
```

#### Initializing a new language:

```
mkdir locales
pybabel init -i locales/messages.pot -d locales -D messages -l en
```

#### Compiling translations (.po -> .mo):

```bash
make i18n-compile
```

#### Updating translated messages (.po) with new extracted messages (.pot):

```bash
make i18n-update
```

## 🙋🏽‍♂️ Contact me

[<img width="30px" title="lleballex | Telegram" src="https://raw.githubusercontent.com/github/explore/main/topics/telegram/telegram.png">](https://t.me/lleballex)
[<img width="30px" title="lleballex | VK" src="https://raw.githubusercontent.com/github/explore/main/topics/vk/vk.png">](https://vk.com/lleballex)
