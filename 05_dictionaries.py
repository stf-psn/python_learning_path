empty_dictionary = {}
print(empty_dictionary);

full_dict = {
    "Stefano": "Pisano",
    "Sailmoiraghi" : "Viganò",
    "Acqua": "Levissima"
}

#key must be unique

print(full_dict['Stefano'])
print(full_dict.keys())
# output is dict_keys(['Stefano', 'Sailmoiraghi', 'Acqua'])

full_dict['Foglio'] = 'Di carta'
print(full_dict)
# output is {'Stefano': 'Pisano', 'Sailmoiraghi': 'Viganò', 'Acqua': 'Levissima', 'Foglio': 'Di carta'}

names_ages = [["John", 35], ["", 38], ["Tim", 27]]
print(names_ages)

a =dict(names_ages)
print(type(a))
# outpout is <class 'dict'>