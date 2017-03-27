import yaml
import pymongo

with open("mongo.yml", 'r') as stream:
        MongoCred = yaml.load(stream)

client = pymongo.MongoClient(MongoCred['MongoDBURI'])
db = client.db
books = db.books

class Book(object):
	idCounter = 1

	def __init__(self, data):
		self.title = data["title"]
		self.author = data["author"]
		self.id = Book.idCounter
		Book.idCounter += 1

	def create(self):
		books.insert({"id":self.id, "title":self.title, "author":self.author});
		# print books.find({"title":1})
		# print "Created"

	# def _response(self):

	# def get(id):




# def show(id):
# 		return books.find({"id":id})	


