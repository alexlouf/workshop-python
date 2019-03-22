import sqlite3

import os
if os.path.exists("ma_base.db"):
  os.remove("ma_base.db")
else:
  print("The file does not exist")


# connexion db
conn = sqlite3.connect('ma_base.db')
cursor = conn.cursor()
conn.execute("PRAGMA foreign_keys = ON")

# on vide la db entiere




# create table User

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
     id_users INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     nom TEXT DEFAULT NULL,
     prenom TEXT DEFAULT NULL,
     email TEXT DEFAULT NULL,
     password TEXT DEFAULT NULL,
     age INTEGER DEFAULT NULL,
     ville TEXT DEFAULT NULL,
     sexe INT DEFAULT NULL,
     photo TEXT DEFAULT NULL,
     description TEXT DEFAULT NULL,
     sport INT DEFAULT NULL,
     voyage INT DEFAULT NULL,
     musique INT DEFAULT NULL
)""")

# create 3 profil of people


cursor.execute("""
INSERT INTO users(nom, prenom, email, password, age, ville, sexe, photo , description, sport, voyage, musique) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
               ("Olivier", "Legrand", "olivier@gmail.com", "1234", 23, "paris", "some url path",
                "Le Lorem Ipsum est simplement du faux texte employé dans la composition et la mise en page avant impression. Le Lorem Ipsum est le faux texte standard de l'imprimerie depuis les années 1500, quand un imprimeur anonyme assembla ensemble des morceaux de texte pour réaliser un livre spécimen de polices de texte. Il n'a pas fait que survivre cinq siècles, mais s'est aussi adapté à la bureautique informatique ",
                1, 0, 0, 1))

cursor.execute("""
INSERT INTO users(nom, prenom, email, password, age, ville, sexe, photo , description, sport, voyage, musique) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
               ("Alexandre", "Louf", "alexandre@gmail.com", "1234", 23, "bordeaux", "some url path",
                "Le Lorem Ipsum est simplement du faux texte employé dans la composition et la mise en page avant impression. Le Lorem Ipsum est le faux texte standard de l'imprimerie depuis les années 1500, quand un imprimeur anonyme assembla ensemble des morceaux de texte pour réaliser un livre spécimen de polices de texte. Il n'a pas fait que survivre cinq siècles, mais s'est aussi adapté à la bureautique informatique ",
                0, 1, 0, 1))

cursor.execute("""
INSERT INTO users(nom, prenom, email, password, age, ville, sexe, photo , description, sport, voyage, musique) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
               ("Clement", "ZOUBI", "clement@gmail.com", "1234", 23, "toulouse", "some url path",
                "Le Lorem Ipsum est simplement du faux texte employé dans la composition et la mise en page avant impression. Le Lorem Ipsum est le faux texte standard de l'imprimerie depuis les années 1500, quand un imprimeur anonyme assembla ensemble des morceaux de texte pour réaliser un livre spécimen de polices de texte. Il n'a pas fait que survivre cinq siècles, mais s'est aussi adapté à la bureautique informatique ",
                1, 0, 1, 0))



conn.commit()


cursor.execute("""SELECT * FROM users""")
users = cursor.fetchall()
print("\n \n Print all USER: \n ")
print(users)


# create table alergie

cursor.execute("""
CREATE TABLE IF NOT EXISTS alergie(
     id_alergie INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     name_alergie TEXT DEFAULT NULL
)""")


cursor.execute("""
INSERT INTO alergie(name_alergie) VALUES(?)""", ("Pollens",))

cursor.execute("""
INSERT INTO alergie(name_alergie) VALUES(?)""", ("Acariens",))

cursor.execute("""
INSERT INTO alergie(name_alergie) VALUES(?)""", ("Moisissures",))

cursor.execute("""
INSERT INTO alergie(name_alergie) VALUES(?)""", ("Poils d’animaux",))

cursor.execute("""
INSERT INTO alergie(name_alergie) VALUES(?)""", ("arachides",))

cursor.execute("""
INSERT INTO alergie(name_alergie) VALUES(?)""", ("blé/gluten",))

cursor.execute("""
INSERT INTO alergie(name_alergie) VALUES(?)""", ("fruits de mer",))

cursor.execute("""
INSERT INTO alergie(name_alergie) VALUES(?)""", ("graines de sésame",))

cursor.execute("""
INSERT INTO alergie(name_alergie) VALUES(?)""", ("lait",))

cursor.execute("""
INSERT INTO alergie(name_alergie) VALUES(?)""", ("noix",))

cursor.execute("""
INSERT INTO alergie(name_alergie) VALUES(?)""", ("œufs",))

cursor.execute("""
INSERT INTO alergie(name_alergie) VALUES(?)""", ("soja",))

cursor.execute("""
INSERT INTO alergie(name_alergie) VALUES(?)""", ("sulfites",))

cursor.execute("""
INSERT INTO alergie(name_alergie) VALUES(?)""", ("moutarde",))

cursor.execute("""
INSERT INTO alergie(name_alergie) VALUES(?)""", ("Soleil",))

cursor.execute("""
INSERT INTO alergie(name_alergie) VALUES(?)""", ("Cosmétiques",))

cursor.execute("""
INSERT INTO alergie(name_alergie) VALUES(?)""", ("Herbes",))












# create table users_alergie_relation
cursor.execute("""
CREATE TABLE IF NOT EXISTS users_alergie(
     id_users INT,
     id_alergie INT,
     PRIMARY KEY (id_users, id_alergie),
     FOREIGN KEY (id_users)  REFERENCES users  (id_users),
     FOREIGN KEY (id_alergie) REFERENCES alergie (id_alergie)
)""")

# deux allergies par personne
cursor.execute("""
INSERT INTO users_alergie(id_users, id_alergie) VALUES(?, ?)""", (1, 2))
cursor.execute("""
INSERT INTO users_alergie(id_users, id_alergie) VALUES(?, ?)""", (1, 3))
cursor.execute("""
INSERT INTO users_alergie(id_users, id_alergie) VALUES(?, ?)""", (2, 4))
cursor.execute("""
INSERT INTO users_alergie(id_users, id_alergie) VALUES(?, ?)""", (2, 5))
cursor.execute("""
INSERT INTO users_alergie(id_users, id_alergie) VALUES(?, ?)""", (3, 6))
cursor.execute("""
INSERT INTO users_alergie(id_users, id_alergie) VALUES(?, ?)""", (3, 7))



# create table compatible_alergie
cursor.execute("""
CREATE TABLE IF NOT EXISTS not_compatible_alergie(
     id_alergie_1 INT,
     id_alergie_2 INT
)""")


cursor.execute("""
INSERT INTO not_compatible_alergie(id_alergie_1, id_alergie_2) VALUES(?, ?)""", (1, 2))


cursor.execute("""
INSERT INTO not_compatible_alergie(id_alergie_1, id_alergie_2) VALUES(?, ?)""", (2, 3))

cursor.execute("""
INSERT INTO not_compatible_alergie(id_alergie_1, id_alergie_2) VALUES(?, ?)""", (2, 6))

cursor.execute("""
INSERT INTO not_compatible_alergie(id_alergie_1, id_alergie_2) VALUES(?, ?)""", (4, 6))

cursor.execute("""SELECT * FROM users_alergie""")
relation_table = cursor.fetchall()
print(" \n \n Print all relation_table: \n ")
print(relation_table)


cursor.execute("""SELECT * FROM alergie""")
alergie = cursor.fetchall()
print("\n \n Print all alergie:  \n ")
print(alergie)

cursor.execute("""SELECT name_alergie FROM alergie INNER JOIN users ON users.id_users = users_alergie.id_users
                                     INNER JOIN users_alergie ON users_alergie.id_alergie = alergie.id_alergie
                                     WHERE users.id_users = 1""")
innerJoin = cursor.fetchall()
print("\n \n Print one users with categorie:  \n ")
print(innerJoin)

cursor.execute("""CREATE TEMPORARY TABLE list_id_user (
    id INT)""")
cursor.execute("""
    SELECT
        ua.id_users
    FROM
        users_alergie ua
    WHERE
        ua.id_alergie NOT IN
            (SELECT
                compatibility_table.id_alergie_2
            FROM
                not_compatible_alergie compatibility_table
            WHERE
                compatibility_table.id_alergie_1 IN
                    (SELECT
                        base_user_allergies.id_alergie
                    FROM
                        users_alergie base_user_allergies
                    WHERE
                        base_user_allergies.id_users=1)
            )
    AND
        ua.id_users != 1
""")


fatRequete = cursor.fetchall()
examples = fatRequete
cursor.executemany("INSERT INTO list_id_user VALUES (?)", examples)
fatRequeteazer = cursor.fetchall()
cursor.execute("SELECT * FROM list_id_user ")
contientIdUser = cursor.fetchall()
cursor.execute("""
SELECT   id
FROM     list_id_user
GROUP BY id
HAVING   COUNT(id) = (SELECT
                        base_user_allergies.id_alergie
                    FROM
                        users_alergie base_user_allergies)
""")
numberTotalIdMatch = cursor.fetchall()
print("\n \n bon tableau:  \n ", numberTotalIdMatch)

conn.close()

