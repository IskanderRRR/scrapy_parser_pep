# Проект парсинга pep

Данный код представляет собой асинхронный парсер документации Python при помощи библиотеки scrapy. Он предоставляет возможность получить информацию о PEP (Python Enhancement Proposal) и их статусах.
### Перед использованием
Клонируйте репозиторий:
```
git clone https://github.com/IskanderRRR/scrapy_parser_pep.git
```
Установите и активируйте виртуальное окружение, установите зависимости:
```
python -m venv venv
```
```
pip install -r requirements.txt
```
### И выполнить команду:
```
cd scrapy_parser_pep
```
```
scrapy crawl pep
```
### Результаты будут сохранены в папке results

- в файле pep_.csv находится информация по всем PEP (их номер, название и статус)
- в файле status_summary_.csv находится информация о колличестве статусов PEP