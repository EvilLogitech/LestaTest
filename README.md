## Тестовое задание на должность - Intern Programmer (Game Logic)
Добрый день. Здесь лежит моё решение тестовых задач. Код в файле main.py, пояснения ниже по тексту.
Также на этом аккаунте мои учебные python-проекты и всё, что я сейчас пишу, если вы захотите сразу посмотреть код побольше.

### Вопрос №1
На языке Python написать алгоритм (функцию) определения четности целого числа,
который будет аналогичен нижеприведенному по функциональности, но отличен по своей сути.
Объяснить плюсы и минусы обеих реализаций.

Функция проверки четности числа отличная по сути от проверки деления без остатка пополам.
Берём двоичное представление числа и проверяем последний знак.
Плюс данного решения - оно не использует арифметические оперции и удовлетворяет идее найти непохожий по сути метод.
Минусы - он дольше. И ещё он менее понятный для чтения кода.

### Вопрос №2
На языке Python написать минимум по 2 класса реализовывающих циклический буфер FIFO.
Объяснить плюсы и минусы каждой реализации.

Реализация любых новых структур всё-равно так или иначе идёт поверх базовых типов.
Так что тут идёт выбор из известных коллекций.
Кортежи не подразумевают изменение - пересоздание отнимает очень много ресурсов.
Множество не подразумевает никакой сортировки и не позволяет хранить дубликаты.
Остаётся список, который всегда хранит порядок данных и словарь, который оптимизирован для операций доступа к данным.

FIFO реализованный через список.
Плюсы - списки всегда сортируются в порядке добавления данных.
Операция добавления в конец списка быстрая.
Занимает меньше памяти, чем Fifo на словаре.
Минусы - операция извлечения данных из списка дольше, чем из словаря.
Можно использовать insert(0, элемент) и pop(), но сути не поменяет.
Долгая вставка по месту, быстрое извлечение. Итоговая скорость не поменяется.

FIFO реализованный через словарь.
Плюсы - операция извлечения из словаря быстрей чем из списка.
Минусы - занимает больше места чем список, плюс нужно место для счётчиков

### Вопрос №3
На языке Python предложить алгоритм, который быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел.
Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным).
Объяснить, почему вы считаете, что функция соответствует заданным критериям.

Скорость алгоритмов не моя сильная сторона, я только начал погружаться в алгоритмы, до этого на предыдущих работах не сталкивался с такой задачей.
В большинстве случаев алгоритм быстрой сортировки один из самых эффективных, поэтому я его реализовал.

Вообще я бы предложил метод sorted() из стандартной библиотеки, поскольку он очень хорошо оптимизирован.
На массивах до 50000 чисел он всегда отрабатывал в несколько раз быстрее моей реализации.
