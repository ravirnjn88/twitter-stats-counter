import requests
import MySQLdb
from dbauth import *
import traceback
from insert_to_table import *

def fun1():
	access_token = "Bearer " + "your access_token"
	url2 = "https://api.twitter.com/1.1/search/tweets.json"
	headers2 = {"Authorization":access_token,"Host":"api.twitter.com","User-Agent":"My Twitter App v1.0.23","Accept-Encoding":"gzip"}

	fo1 = open("id","r+")
	a = fo1.read()
	if(a == ""):
		max_id = ""
		b = max_id
	else:
		max_id = int(a)
		b = max_id
	fo1.close()

	fo2 = open("id","w")
	fo2.close()

	try:
		params = {"q":"#JazbaaTrailer","max_id":max_id,"count":"100","include_entities":1}
		r = requests.get(url2,headers=headers2,params=params)
		y = r.json()
		n =0
		print max_id
		print "\n"
		for elements in y["statuses"]:
			n = n+1
			post_date = elements["created_at"].encode("utf8").encode("utf8")
			post_id = elements["id"]
			if (post_id  < max_id):
				max_id = post_id
			post_content = elements["text"].encode("utf8").replace('"',"'")
			user_id = elements["user"]["id"]
			user_name = elements["user"]["name"].encode("utf8")
			screen_name = elements["user"]["screen_name"].encode("utf8")
			print "---",post_date
			print "---",post_id
			print "---",post_content
			print "---",user_id
			print "---",user_name
			print "---",screen_name

			if (check_user_id(user_id)!=1):
				insert_user_id(user_id,user_name,screen_name)
				insert_post_id(user_id,post_id,post_date,post_content)
				print "-------------New Inserted------------"
			else:
				if (check_post_id(post_id)!=1):
					increase_count(user_id)
					insert_post_id(user_id,post_id,post_date,post_content)
					print "----------------Incremented-----------"
				else:
					print "-------------Alredy in post id------------------------"

			print "-------------"

		#max_id = y["search_metadata"]["next_results"].split("=")[1].replace("&q","")
		print max_id
		fo2 = open("id","a")
		fo2.write(str(post_id))
		fo2.close()
		print n
	except:
		traceback.print_exc()
		fo2 = open("id","a")
		try:
			if(max_id > 0):
				fo2.write(max_id)
			else:
				fo2.write(str(b))
		except:
			fo2.write(str(b))
		fo2.close()

i =20
while(i>0):
	fun1()
	i = i-1