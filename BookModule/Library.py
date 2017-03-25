import yaml

from pymongo import MongoClient
client = MongoClient()
db = client.primer
coll = db.dataset

class Book(object):
	idCounter = 1

	def __init__(self, data):
		self.title = data["title"]
		self.author = data["author"]
		self.id = Book.idCounter
		Book.idCounter += 1

	def create(self):
		# -> guardar en mongodb
		print "Created"

	# def _response(self):

	# def get(id):

	# def show():
		
