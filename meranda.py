from flask import Flask
from flask_restful import Api, Resource
import json

#inisial objek flask
app = Flask(__name__)
#inisial objek flask_restful
api = Api(app)

class Home(Resource):
    def get(self):
        #buka file json
        home = open("home.json", "r")
        #parsing data json
        #parsing adalah proses membaca file json mulai baris awal sampai akhir
        jsonHome = json.load(home)
        #mengembalikan nilai dari jsonHome yang sudah di parsing sebelumnya
        return {"home": jsonHome}

class Business(Resource):
    def get(self):
        business = open("business.json", "r")
        jsonBusiness = json.load(business)
        return {"business": jsonBusiness}

class Categories(Resource):
    def get(self):
        categories = open("categories.json", "r")
        jsonCategories = json.load(categories)
        return {"categories": jsonCategories}

class Contact(Resource):
    def get(self):
        contact = open("contact.json", "r")
        jsonContact = json.load(contact)
        return {"contact": jsonContact}

class Design(Resource):
    def get(self):
        design = open("design.json", "r")
        jsonDesign = json.load(design)
        return {"design": jsonDesign}
    
class Healt(Resource):
    def get(self):
        healt = open("healt.json", "r")
        jsonHealt = json.load(healt)
        return {"healt": jsonHealt}

class Politics(Resource):
    def get(self):
        politics = open("politics.json", "r")
        jsonPolitics = json.load(politics)
        return {"politics": jsonPolitics}

class Sport(Resource):
    def get(self):
        sport = open("sport.json", "r")
        jsonSport = json.load(sport)
        return {"sport": jsonSport}

#setup resource
api.add_resource(Home, '/home/')
api.add_resource(Business, '/business/')
api.add_resource(Categories, '/categories/')
api.add_resource(Contact, '/contact/')
api.add_resource(Design, '/design/')
api.add_resource(Healt, '/healt/')
api.add_resource(Politics, '/politics/')
api.add_resource(Sport, '/sport/')

if __name__ == '__main__':
    app.run()