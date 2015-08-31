import json

auth = """{
		"database"   : "database-name",
		"user"     : "root",
		"password" : "database-password",
		"host"     : "localhost"
		}"""
a = json.loads(auth)
host = a.get("host")
user = a.get("user")
passwd = a.get("password")
database = a.get("database")