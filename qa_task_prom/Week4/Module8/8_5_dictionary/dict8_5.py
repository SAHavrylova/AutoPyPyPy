# Опрацювання словників - перевірка наявності ключа

user = {
    "name": "Sergii",
    "age": 100500,
    "profession": "Golf Player",
    "country": "Ukraine"
}

if "name" in user:
    print(user["name"])
else:
    print("No 'name' key on your dict")

if "company" in user:
    print(user["company"])
else:
    print("No 'company' key on your dict")
