import requests
import json
import bd

#jsonlist = json.dumps(response) #<= transforma a resposta em um string json
#json_obj = json.loads(jsonlist) #<= convete essa string em um objeto


eventos = []


database = bd.mydict
for id in database:
	db_id = database[id]
	finalstring = ''
	event_check = [i for i in range(4)]
	for index in db_id:
		db_index = db_id[index]
		if index == 'event-name':
			finalstring += db_index
		if index == 'date':
			finalstring += db_index
			event_check.remove(1)
		if index == 'departament':
			finalstring += db_index
			event_check.remove(2)
		if index == 'hour':
			finalstring += db_index
			event_check.remove(3)
	print(finalstring)
