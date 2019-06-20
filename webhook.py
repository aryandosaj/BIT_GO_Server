import pickle
from flask import Flask, request, make_response, jsonify
import scrap
app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def result():
    data = request.form
    print(data)
    query = scrap.get_detail(data['Roll'],data['Password'])
    return make_response(jsonify(query))

# if(__name__==__main__):
app.run(debug=True)