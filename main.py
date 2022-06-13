from requests import delete
from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import update
from telegram import Contact


engine = create_engine("sqlite:///./contacts.db")

Session = sessionmaker(bind=engine)

Base = declarative_base()


class Contacts(Base):
    __tablename__ = "Contacts"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    phone = Column(Integer)
    email = Column(String)
    adress = Column(String)

    def __init__(self, first_name, last_name, phone, email, adress):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.adress = adress

    # def __str__(self):
    #     return f"{self.first_name} | {self.phone}"


def add_contact():
    first_name = input("Enter first name: ")
    last_name = input("Entet last name: ")
    phone = int(input("Enter phone number: +998 9"))
    email = input("Enter email adress: ")
    adress = input("Enter adress: ")

    session = Session()

    session.add(Contacts(first_name, last_name, phone, email, adress))
    print("Succesfully added!")

    session.commit()
    session.close()


def delete_contact():
    session = Session()
    session.query(Contacts).all()

    name = input("Enter first name: ")
    surname = input("Enter last name: ")

    session.query(Contacts).filter(
        Contacts.first_name == name and Contacts.last_name == surname
    ).delete()
    session.commit()


def show_all():
    session = Session()
    contacts = session.query(Contacts).all()

    for contact in contacts:
        print(
            f"{contact.first_name} | {contact.last_name} | {contact.phone} | {contact.email} | {contact.adress}\n"
        )
    session.commit()


def update_contacts():

    name = input("Enter name: ")
    surname = input("Enter last name: ")

    session = Session()
    # contacts = session.query(Contacts).all()
    session.query(Contacts).filter(
        Contacts.first_name == name and Contacts.last_name == surname
    ).update({Contacts.first_name == name, Contacts.last_name == surname})

    session.commit()


# add_contact()
# delete_contact()
# show_all()
# update_contacts()
# Base.metadata.create_all(engine)
