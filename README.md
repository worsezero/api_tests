a# API Tests — JSONPlaceholder

Автоматизированные API-тесты на Python с отчётами Allure.

## Стек

- Python 3
- pytest
- requests
- allure-pytest

## Что тестируется

Тесты покрывают основные HTTP-методы REST API ([jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com)):

| Тест | Метод | Endpoint |
|------|-------|----------|
| Проверка статус-кода | GET | /posts/1 |
| Проверка id поста | GET | /posts/1 |
| Проверка типа title | GET | /posts/1 |
| Создание поста | POST | /posts |
| Удаление поста | DELETE | /posts/1 |
| Получение комментариев | GET | /comments?postId=1 |
| Обновление поста | PUT | /posts/1 |

## Установка

```bash
pip install requests pytest allure-pytest
```

## Запуск тестов

```bash
pytest test_api.py -v
```

## Запуск с Allure отчётом

```bash
pytest test_api.py -v --alluredir=allure-results
allure serve allure-results
```

## Структура

```
api_tests/
├── test_api.py       # API тесты
└── README.md
```

## Автор

[worsezero](https://github.com/worsezero)
