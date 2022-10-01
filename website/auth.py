from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from urllib.request import urlopen
from datetime import timedelta
import json, requests
import pandas as pd
from tabulate import tabulate


auth = Blueprint('auth', __name__)



@auth.route('/login', methods=['GET','POST'])
def login():

    if request.method == "POST":
        id_form = request.form['id']
        try:
            r = requests.post("https://1fa9eparjd.execute-api.ap-southeast-1.amazonaws.com/dev/resource-get_user_from_db", json=
                    {
                        "user_id": int(id_form)
                    })
            result_status = r.status_code
            if result_status == 200:
                result = r.json()
                try:
                    user_id = result["body"]["user_id"]
                    firstname = result["body"]["firstname"]
                    lastname = result["body"]["lastname"]
                    return firstname + " " + lastname
                except:
                    return "User does not exist."
            else:
                return "An error occured. Response code: " + result_status
        except requests.exceptions.RequestException as e:
            return e
    else:
        return render_template("login.html")


    """ 
    EXAMPLE START
    if request.method == "POST":
        session.permanent = True
        fname_value = request.form["fname_form"]
        session["fname"] = fname_value
        return redirect(url_for("auth.logged_in"))
    else:
        if "fname" in session:
            return redirect(url_for("auth.logged_in"))
            
        return render_template("login.html")
    EXAMPLE END
    """
@auth.route('/fname',)
def logged_in():
    """
    EXAMPLE START
    if "fname" in session:
        fname = session["fname"]
        return f"<h1>{fname}</h1>"
    else:
        return render_template("login.html")
    EXAMPLE END
    """
    

@auth.route('/logout')
def logout():
   # session.pop("fname", None)
    return redirect(url_for("auth.login"))



@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    return render_template("sign_up.html")



@auth.route('/page1', methods=['GET'])
def page1():
    api_url = "https://1fa9eparjd.execute-api.ap-southeast-1.amazonaws.com/test/resource-test-get"
    response = urlopen(api_url)
    data_json = json.loads(response.read())

    firstname = data_json["body"]["firstname"]
    lastname = data_json["body"]["lastname"]

    return firstname + " " + lastname



@auth.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        return insert()
    
    return render_template("login.html")



@auth.route('/insert_output', methods=['GET','POST'])
def insert_output():
    
    request_body = {
        "user_id" : 6,
        "firstname" : "Amber",
        "lastname" : "Heard"
    }
    process = requests.post("https://1fa9eparjd.execute-api.ap-southeast-1.amazonaws.com/dev/resource-post-db", json=request_body)
    response_code = process.json()

    return response_code

@auth.route('/table', methods=['GET'])
def table():


    api_url = "https://1fa9eparjd.execute-api.ap-southeast-1.amazonaws.com/dev/resource-get_table_data"
    response = urlopen(api_url)
    data_json = json.loads(response.read())


    data = data_json["body"]
    data_count = int(len(data))

    for i in range(data_count):
        t_data = data_json["body"][i]
        i += 1
    
    return t_data
       
    
    
   
    
     
       

    
    #x =  pd.DataFrame(val2, columns=["time", "temperature", "quality"])

    
 
    """
    process = requests.get("https://1fa9eparjd.execute-api.ap-southeast-1.amazonaws.com/dev/resource-get_table_data")
    table_data = process.json()
    response_code = process.status_code
    x = table_data['items']
    """
    



    



    

