import connection


class Author:
    def __init__(self, first_name, last_name, about, email, phone_number):
        self.connection = connection.Connection(host="localhost", db_name="grow_db")
        self.first_name = first_name
        self.last_name = last_name
        self.about = about
        self.email = email
        self.phone_number = phone_number

    def save(self):
        with self.connection as c:
            cursor = c.cursor()
            cursor.execute("""insert into grow_author (firstName, lastName, about, email, phone_number)
                                values (%s, %s, %s, %s, %s)""", (self.first_name,
                                                                 self.last_name,
                                                                 self.about,
                                                                 self.email,
                                                                 self.phone_number) )
            c.commit()


author = Author("Alex", "Klein", "Photographer, traveller", "alex@klein.com", "467214")
author.save()