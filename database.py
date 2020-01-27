from model import Base, Cat

from flask import url_for

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


# def query_all():
# 	cat=session.query(Cat).all()
# 	return cat

def add_cat(name, title, story, img):
	print("added a cat!")
	# cat_ob = Cat(name=name, title=title, story=story)
	cat_ob = Cat(
		name=name,
		title=title,
		story=story,
		img=img)
	session.add(cat_ob)
	session.commit()

add_cat("Meowfioso", "Catnip Dealer", "He dealt catnip in small neighborhoods until he became international", "static/img/slider/fioso.jpg")
add_cat("Napawleon", "General in the Dark", "The bodies laid before him were not restricted to the battlefield", "static/img/slider/napawleon.jpg")
add_cat("Mer", "The Cat That Walks On Water", "Drowned her owners in the bathtub", "static/img/slider/mer.jpg")
add_cat("Purrl", "Art Thief and Forger", "Stole famous paintings from museums and replaced them with a replica in which she replaced the humans with cats", "static/img/slider/Purrl.jpg")
add_cat("Dante", "The Inferno", "He just loved to set things on fire. He was slightly odd that way", "static/img/slider/dante.jpg")
add_cat("Meow Meow", "The DJ", "He didn't committ any crimes, but the mean parties he throws deserve a shoutout", "static/img/slider/dj.jpg")


# add_cat("Meowfioso", "Catnip Dealer", "He dealt catnip in small neighborhoods until he became international", href={{url_for('static', filename="img/slider/fioso.jpg")}})
# add_cat("Napawleon", "General in the Dark", "The bodies laid before him were not restricted to the battlefield ", href={{url_for('static', filename="img/slider/fioso.jpg")}})

def query_all():
	cat = session.query(Cat).all()
	return cat

