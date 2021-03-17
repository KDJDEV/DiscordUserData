import flask
from flask import Flask
from flask_restful import Api, Resource
import requests
from os import environ
token = environ['token']

app = flask.Flask(__name__)
api = Api(app)

class GetUserInfo(Resource):
	def get(self, userid):
		data = requests.get(f"https://discord.com/api/v8/users/{userid}/profile", headers={"authorization":token})
		json = data.json()
		return json

api.add_resource(GetUserInfo, "/id/<string:userid>")
if __name__ == "__main__":
	app.run()
