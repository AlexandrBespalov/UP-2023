# Описание работы программы

###### ***Задание:*** Парсер сайта РБК, выбираем в интерфейсе поле для запроса, вводим тему (если такой нет, вывести ошибку) и по ней выдать заголовки новостей по текущей дате.

При запуске программы выполняется:

1. Парсинг новостей по текущей дате в allnews.csv;
2. Открытие интерфейса с полем ввода конкретной темы (Политика, Общество, Бизнес);
3. При нажатии на кнопку выполняется:
    + Проверка введенного текста на соответствие имеющимся темам;
    + При наличии новостей по заданной теме выдает в терминал их заголовки;
    + При отсутствии новостей по заданной теме выдает ошибку: ***Ошибка, новости не найдены.***