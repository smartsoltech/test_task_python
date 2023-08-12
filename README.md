## Разработка скрипта для категоризации пользовательских запросов
***
### Задание:

#### Вам необходимо написать скрипт на языке Python, который будет категоризировать письма, представленные в формате CSV. Вам будет отправлен CSV-файл с перемешанными обезличенными письмами из разделов: Security, Refunds, Troubleshooting, Account, Advertising and Collaboration, Limits, Payments, Features.

---

Требования:

1. Вам нужно разработать скрипт, который будет считывать содержимое CSV-файла и категоризировать каждое письмо в соответствии с его содержимым. Категория должна быть определена на основе ключевых слов, содержащихся в тексте письма.
2. Проанализируйте содержимое и выявите зависимости.
3. Создайте словарь с ключевыми словами для каждой категории. 
4. Скрипт должен открывать CSV-файл, считывать каждое письмо и проверять его содержимое на наличие ключевых слов для каждой категории.
5. Письмо должно быть отнесено к одной или нескольким категориям, если оно содержит соответствующие ключевые слова и корни к ним. 
6. Результаты категоризации должны быть сохранены в новом CSV-файле или выведены на экран в удобочитаемом формате.
7. Обратите внимание, что ключевые слова могут быть регистронезависимыми, то есть их наличие в письме должно быть определено без учета регистра.
8. Дополнительным плюсом будет реализация обработки исключений, чтобы скрипт не завершался с ошибкой при некорректной структуре CSV-файла или отсутствии файла.
___
Конечно! Ниже представлена документация к вашему заданию в формате Markdown:

---

# Документация к скрипту категоризации писем из CSV

## Описание

Скрипт предназначен для категоризации писем, представленных в формате CSV. Письма категоризируются на основе их содержания в следующие категории: Security, Refunds, Troubleshooting, Account, Advertising and Collaboration, Limits, Payments, Features.

## Входные данные

- Файл в формате CSV, содержащий перемешанные обезличенные письма. Каждая строка представляет собой отдельное письмо. Формат и структура файла будут дополнительно уточнены.

## Выходные данные

- Файл в формате CSV с категоризированными письмами. Каждое письмо будет снабжено меткой категории.

## Использование

1. Загрузите исходный CSV-файл с письмами.
2. Запустите скрипт.
3. Получите файл с категоризированными письмами.

## Примечание

Для выполнения категоризации писем потребуется разработать или использовать алгоритм или модель машинного обучения, способную анализировать содержание письма и определять его категорию на основе заданных критериев или обученных данных.
