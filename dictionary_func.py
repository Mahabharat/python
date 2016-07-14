dictionary={1:"One",2:"Two",3:"Three"}
print(len(dictionary))
print(dictionary.keys())
print(dictionary.values())

new={4:"Four",5:"Five"}
dictionary.update(new)
print(dictionary)

dictionary.clear()
print(dictionary)

