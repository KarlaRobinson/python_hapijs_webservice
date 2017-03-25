from pymongo import MongoClient
client = MongoClient()
db = client.primer

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

	def _response(self):
		self.ok = True

	def get(id):
		print
