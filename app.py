from database import *
from flask import Flask, render_template,url_for,request,redirect
from flask import session as login_session
import requests, json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template("index.html")


@app.route('/killers', methods=['GET', 'POST'])
def killers():

	return render_template("home-2.html", cats = query_all())


@app.route('/danger', methods=['GET', 'POST'])
def danger():
	return render_template("portfolio.html")

@app.route('/safety', methods=['GET', 'POST'])
def safety():
	return render_template("blog.html")



@app.route('/api', methods=['GET', 'POST'])
def api():
	if request.method == "POST":
		print("a")
		url=request.form["url"]
		headers = {'Authorization': 'Key f37cdfbecf4b4cd69c8cac60b9d89d50'}
		api_url = "https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/outputs"
		data ={"inputs": [
		{
		"data": {
		"image": {
		"url": url
		}
		}
		}
		]}
		response = requests.post(api_url, headers=headers, data=json.dumps(data))
		response_dict=json.loads(response.content)
		print(response_dict["outputs"][0]["data"]["concepts"])
		catss="This is not a cat"
	
		for item in response_dict["outputs"][0]["data"]["concepts"]:
			print(item["name"])
			if (item["name"])== "cat":
				catss=" This is a cat"
				
				break

			# Check if there is cat-- true/ false write to user

		return render_template("contact.html", is_cat= catss)
	else:
		return render_template("contact.html") 

	

# api()

if __name__ == '__main__':
   app.run(debug = True)