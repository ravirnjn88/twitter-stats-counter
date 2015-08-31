import MySQLdb
from dbauth import *
import traceback

#check user_id in TWITTER_USER_ID
def check_user_id(user_id):
	db = MySQLdb.connect(host,user,passwd,database)
	cur = db.cursor()
	sql_query = """ SELECT * FROM TWITTER_USER_ID WHERE USER_ID= "%s" """ % (user_id)
	#print sql_query
	cur.execute(sql_query)
	result = cur.rowcount
	#print result
	db.close()
	return result

def check_post_id(post_id):
	db = MySQLdb.connect(host,user,passwd,database)
	cur = db.cursor()
	sql_query = """ SELECT * FROM TWITTER_POST_ID WHERE POST_ID= "%s" """ % (post_id)
	#print sql_query
	cur.execute(sql_query)
	result = cur.rowcount
	#print result
	db.close()
	return result

# insert in TWITTER_USER_ID
def insert_user_id(user_id,user_name,screen_name):
	db = MySQLdb.connect(host,user,passwd,database)
	cur = db.cursor()
	sql_query = """INSERT INTO TWITTER_USER_ID ( USER_ID, USER_NAME, SCREEN_NAME) VALUES ("%s","%s","%s")""" % (user_id, user_name, screen_name)
	cur.execute(sql_query)
	db.commit()

# insert in TWITTER_POST_ID
def insert_post_id(user_id,post_id,post_date,post_content):
	db = MySQLdb.connect(host,user,passwd,database)
	cur = db.cursor()
	sql_query = """INSERT INTO TWITTER_POST_ID ( USER_ID, POST_ID, POST_DATE, POST_CONTENT) VALUES ("%s","%s","%s","%s")""" % (user_id, post_id, post_date, post_content)
	cur.execute(sql_query)
	db.commit()

# increase count in TWITTER_USER_ID
def increase_count(user_id):
	db = MySQLdb.connect(host,user,passwd,database)
	cur = db.cursor()
	sql_query = """SELECT COUNT FROM TWITTER_USER_ID WHERE USER_ID = "%s" """ % (user_id)
	cur.execute(sql_query)
	z = cur.fetchone()[0] +1
	sql_query2 = """UPDATE TWITTER_USER_ID SET COUNT = "%s" WHERE USER_ID = "%s" """ % (z,user_id)
	cur.execute(sql_query2)
	db.commit()
	return z

#IF RUN AS STAND ALONE SCRIPT
if __name__ == "__main__":
	#insert_user_id(1234,"Ravi Ranjan","ravirnjn88")
	#insert_post_id(1234,142637373,"12 4 2015","oh my god")
	print increase_count(1234)
	print check_user_id(12345)
