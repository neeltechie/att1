from flask import Flask
from flask_restplus import Resource, Api
import time
from functools import cached_property

app = Flask(__name__)
api = Api(app)


@api.route("/index")
class HelloWorld(Resource):
    def get(self):
        return {"time": time.asctime(time.localtime())}, 200


if __name__ == "__main__":
    app.run(debug=True)
