# from folder_directory.filename import Class name
from prac_6.programming_language import ProgrammingLanguage

# This creates "instances" of the programming language class
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

# This will print True if python has dynamic typing (it does)
print(ProgrammingLanguage.is_dynamic(python))

# Prints all the information on this language
print(python)

# Print all languages that have dynamic typing
programming_languages = [ruby, python, visual_basic]
print("The dynamically typed languages are:")
for programming_language in programming_languages:
    if programming_language.is_dynamic():
        print(programming_language.name)


