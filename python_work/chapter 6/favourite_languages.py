favourite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python"
}

language = favourite_languages["sarah"].title()
print(f"Sarah's favourite language is {language}.")

'''
You do not need to pass the 2nd parameter. If the 2nd parameter is not passed,
then 'None' will be returned which represents and means that a value has not
been set 
'''
# my_language = favourite_languages.get("jarryd")
my_language = favourite_languages.get("jarryd", "User does not exist.")
print(my_language)

print()
for name, language in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}.")

# .keys() is the default methods called. You can actually exclude calling 
# .keys() and it should be called automatically
print()
for name in favourite_languages.keys():
    print(name.title())

print()
friends = ["phil", "sarah"]
for name in favourite_languages:
    print(f"Hi {name}.")

    if name in friends:
        language = favourite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

print()
if "erin" not in favourite_languages.keys():
    print("Erin, please take our poll!")

print()
for name in sorted(favourite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print()
print("The following languages have been mentioned:")
for language in set(favourite_languages.values()):
    print(language.title())

# A set is a list that contains unique values only. It automatically removes
# duplicate values
print()
my_set = {"python", "rust", "c", "python"}
print(my_set)

print()
favourite_languages = {
    "jen": ["python", "rust"],
    "sarah": ["c"],
    "edward": ["rust", "go"],
    "phil": ["python", "haskell"]
}

for name, languages in favourite_languages.items():
    print(f"\n{name.title()}'s favourite languages are:")
    for language in languages:
        print(f"\t{language.title()}")