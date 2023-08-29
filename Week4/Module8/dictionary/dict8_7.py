'''
Correct behaviour
key_list[0] = "country"
TypeError: 'dict_keys' object does not support item assignment
''' 

user = {
    "name": "Sergii",
    "age": 100500,
    "profession": "Golf Player",
    "country": "Ukraine"
}
key_list = user.keys()
print(key_list)
key_list[0] = "country"