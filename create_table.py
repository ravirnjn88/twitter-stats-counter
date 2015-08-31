import MySQLdb
from dbauth import *

def create_table():
	db = MySQLdb.connect(host,user,passwd,database)
	cur = db.cursor()

	#Create main table count contains no of times the user has tweeted with the tag
	sql_query = """CREATE TABLE TWITTER_USER_ID (
					USER_ID BIGINT PRIMARY KEY NOT NULL,
					USER_NAME TEXT NOT NULL,
					SCREEN_NAME TEXT NOT NULL,
					COUNT INT DEFAULT 1)"""

	#Create small image links table
	sql_query2 = """CREATE TABLE TWITTER_POST_ID (
					ID INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
					USER_ID BIGINT NOT NULL,
					POST_ID BIGINT NOT NULL,
					POST_DATE TEXT NOT NULL,
					POST_CONTENT TEXT NOT NULL,
					FOREIGN KEY (USER_ID) REFERENCES TWITTER_USER_ID(USER_ID))"""

	cur.execute(sql_query)
	cur.execute(sql_query2)
	cur.close()

create_table()