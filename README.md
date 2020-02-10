### Тестовое задание для кандидатов на должность Python/Django разработчика

## Необходимо разработать веб-приложение, обеспечивающее возможность работы со справочником устройств оповещения:
    1. Каждое устройство оповещения имеет следующие параметры
        a. Тип устройства (сирена или громкоговоритель)
        b. Адрес размещения (строка)
        c. Широта (число с 6 знаками после запятой)
        d. Долгота (число с 6 знаками после запятой)
        e. Радиус зоны звукопокрытия (целое число в метрах)
    2. Открытая часть приложения должна быть доступна любому пользователю в форме веб-сайта и обеспечивать следующие возможности:
        a. Просмотр списка существующих в системе устройств оповещения с разбиением на страницы
        b. Добавление новых устройств оповещения с индикацией ошибок заполнения формы
    3. Административная часть приложения должна обеспечивать возможность выполнения операций добавления, редактирования и удаления устройств оповещения
    4. Приложение должно реализовывать REST API для работы со справочником устройств оповещения: получение списка, добавление, удаление, обновление, фильтрация по параметрам, поиск.
    5. Разместить результат работ в открытом доступе. Например, с использованием pythonanywhere или любым другим вариантом, который позволит посмотреть приложение в действии.
    
## Требования к решению:
    • Веб-приложение должно быть реализовано на языке Python с использованием Django
    • REST API должно быть реализовано с использованием Django REST Framework
    • Приложение должно использовать в качестве СУБД PostgreSQL
    • Приложение должно использовать Class-based views


