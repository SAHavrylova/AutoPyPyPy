'''
Описати клас БазаДанних (Database), який задовольняє наступні умови:

Конструктор класу приймає обов'язковий параметр "Ім'я бази даних" (database_name) і зберігає його значення, як атрибут об'єкту.
В конструкторі оголошений атрибут об'єкту "Під'єднано до бази даних" (connected_to_database), який за замовчування має значення False.
В класі оголошений атрибут класу "Виконані Команди" (executed_commands) із значенням по замовчуванню - пустий список, який буде наповнюватися командами, які будуть виконані будь-яким об'єктом класу Database.
Клас має наступні статичні методи:
перевести в нижній регістр (to_lower) з обов'язковим параметром str, який повертає в результаті роботи введене в параметр str значення переведене в нижній регістр.
Клас має наступні методи класу:
Додати до списку виконаних команд (add_to_executed_commands), з обов'язковим параметром command. Задача методу додати до списку виконаних команд (атрибут класу - executed_commands) значення параметра command.
Клас має наступні методи об'єкту:
Під'єднатися до бази даних (connect_to_database), задача якого змінити значення атрибуту об'єкта connected_to_database на True та вивести на екран повідомлення "Під'єднано до бази даних";
Виконати команду (execute_command) з обов'язковим параметром "Команда" (command). Задача методу вивести на екран введене значення параметра command та додати цю команду до атрибуту класу executed_commands за допомогою методу класу add_to_executed_commands.
Додаткові умови:
Ім'я бази даних (input_database_name) вводиться користувачем з клавіатури;
Команда для виконання (input_command_to_execute) вводиться користувачем з клавіатури;
Зауважте: під командою мається на увазі довільний текст.
Конструктор має лише два параметри: self та database_name;
Обов'язково використовуйте декоратори;
Використовуйте запропоновані назви методів і класів.
Очікуваний результат виконання програми:

Для набору вхідних даних ("Користувачі", "Створити Користувача") – текст на екрані:
"Користувачі"
False
"Під'єднано до бази даних"
True
[]
"створити користувача"
['створити користувача']
Для набору вхідних даних ("Зарплата", "Видати 100500ГРН Кожному") – текст на екрані:
"Зарплата"
False
"Під'єднано до бази даних"
True
[]
"видати 100500грн кожному"
['видати 100500грн кожному']
Увага!

Не змінюйте наведений стартовий код. Своє рішення набирайте під коментарем # your code goes here
Для позначення блоків коду використовуйте відступи в 4 пробіли.
Будьте уважні з вхідними даними.
Не використовуйте без нагальної потреби будь-які зайві символи в тексті, який ви виводите на екран - можуть виникати непередбачувані помилки під час автоматичної перевірки.
'''

input_database_name = input("Введіть ім'я бази даних ")
input_command_to_execute = input("Введіть команду для виконання ")


class Database:
    executed_commands = []
    def __init__(self, database_name):
        self.database_name = database_name
        self.connected_to_database = False

    @staticmethod
    def to_lower(string):
        return string.lower()
    
    @classmethod
    def add_to_executed_commands(cls, command):
        cls.executed_commands.append(command)
    
    def connect_to_database(self):
        self.connected_to_database = True
        print("Під'єднано до бази даних")
    
    def execute_command(self, command):
        print(command)
        self.add_to_executed_commands(command)


db = Database(input_database_name)
print(db.database_name)
print(db.connected_to_database)

db.connect_to_database()
print(db.connected_to_database)
print(Database.executed_commands)

lower_command = Database.to_lower(input_command_to_execute)
db.execute_command(lower_command)
print(Database.executed_commands)