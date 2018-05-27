class Person(object):
    def __init__(self, first_name, last_name, phone_number, birth_year, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.birth_year = birth_year
        self.email = email

    def get_full_name(self):
        return self.first_name + " " + self.last_name

john = Person(first_name="John", last_name="Clark", phone_number=89348239429, birth_year=1979, email="john@clark.com")
marissa = Person(first_name="Marissa", last_name="Mayer", phone_number=83483204032, birth_year=1978, email="marissa@yahoo.com")
bruce = Person(first_name="Bruce", last_name="Wayne", phone_number=902432309443, birth_year=1939, email="bruce@batman.com")


contact_book = [john, marissa, bruce]

for person in contact_book:
    print person.first_name, person.last_name, person.birth_year, person.email
    print person.get_full_name()
    print ""  # empty line