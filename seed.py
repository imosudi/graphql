from app import db, User, Post

# Application DB migrated to existing remote database 
'''db.create_all()     # create tables from models

user1 = User(
    name="Mosudi Isiaka",
    email='imosudi@gmail.com'
)
user2 = User(
    name="Mosud Olukayode",
    email='imosudi@yahoo.com'
)

post1 = Post()
post1.title = "Blog Post Title 1"
post1.body = "This is the first blog post 1"
post1.author = user1

post2 = Post()
post2.title = "Blog Post Title 2"
post2.body = "This is the 2nd blog post 2"
post2.author = user2

post3 = Post()
post3.title = "Blog Post Title 3"
post3.body = "This is yet another blog post 3"
post3.author = user1'''

db.session.add(post1)
db.session.add(user1)
db.session.add(user2)
db.session.add(post2)
db.session.add(post3)
db.session.commit()

print(User.query.all())
print(Post.query.all())
