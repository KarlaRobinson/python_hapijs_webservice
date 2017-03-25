import Library


# book = Library.Book({
# 	title: 'sd',
# 	author: 'asd'
# 	})

book = Library.Book({
	'title': 'sd',
	'author': 'asd'
	})

book.create()

# print book._response.ok == true
# print book.id


#llamar de mongodb
# book = Library.Book.get(1)

# print book.title
# print book.author
# print book._response.ok == true