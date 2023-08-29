# Додавання елементів до словника

user = {"name": "Sergii"}
user["age"] = 100500 # type: ignore
print(user)

user["profession"] = "Golf Player"
print(user)

key = "country"
user[key] = "Ukraine"
# те саме що і user["country"] = "Ukraine"
print(user)