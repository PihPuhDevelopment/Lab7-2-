import MySQLdb
from MySQLdb.constants import FIELD_TYPE

db = MySQLdb.connect(host="localhost", db="grow_db", read_default_file="~/.my.cnf")
cursor=db.cursor()
cursor.execute("select article_id, author_id, pubdate, likes from articles")
result = cursor.fetchall()

for x in result:
    print(x)