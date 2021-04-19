import firebase_admin
from firebase_admin import credentials,firestore

import flask
from flask import abort,jsonify,request,redirect
import json
import requests
app=flask.Flask(__name__)
if not firebase_admin._apps:
    cred = credentials.Certificate('zomato_api.json') 
    default_app = firebase_admin.initialize_app(cred)
store=firestore.client()
@app.route('/addRESTAURANT',methods=['POST'])
def addRESTAURANT():
    data=request.get_json(force=True)
    dit={}
    dit["name"]=data.get("name")
    dit["mobile"]=data.get("mobile")
    dit["typ"]=data.get("typ")
    dit["address"]=data.get("address")
    dit["location"]={'lat':data.get("lat"),'lng':data.get("lng")}
    dit["rest_id"]=data.get("rest_id")
    dit["image"]=data.get("imageURL")
    dit['created_at']=firestore.SERVER_TIMESTAMP

    store.collection("RESTAURANTS").add(dit)


    return jsonify({"response":200})
if __name__=='__main__':
    app.run(host='127.0.0.1',port=5001,debug=False)
    