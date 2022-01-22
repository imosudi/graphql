from app import db, User, Post

db.create_all()     # create tables from models

user1 = User(
    name="Sadhan Sarker",
    email='cse.sadhan@gmail.com'
)

post1 = Post()
post1.title = "Blog Post Title 1"
post1.body = "This is the first blog post 1"
post1.author = user1

db.session.add(post1)
db.session.add(user1)
db.session.commit()

print(User.query.all())
print(Post.query.all())