import shutil

from faker import Faker

fake = Faker('en_US')

contents = ""

range_gen = range(100)

print(type(range_gen))

iterator = iter(range_gen)

print(type(iterator))

existing = ""

while True:

    try:
        i = next(iterator)
    except StopIteration:
        break


    email = fake.email()
    phone_number = fake.phone_number()

    contents += fake.paragraph()
    contents += email
    contents += fake.paragraph()
    contents += fake.ssn()
    contents += fake.sentence()
    contents += phone_number
    contents += fake.paragraph()
    if i % 7 == 0:
        contents += email
        contents + fake.sentence()

    if i % 9 == 0:
        contents += phone_number
        contents += fake.paragraph()

    if i % 5 == 0:
        existing += email + "\n"
        existing += phone_number + "\n"


    contents += "\n"

with open("potential-contacts.txt", "w+") as f:
    f.write(contents)

shutil.copy('potential-contacts.txt', '../../lab/assets/potential-contacts.txt')

with open("existing-contacts.txt", "w+") as f:
    f.write(existing)

shutil.copy('existing-contacts.txt', '../../lab/assets/existing-contacts.txt')




