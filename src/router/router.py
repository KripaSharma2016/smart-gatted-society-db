
# it will accept all rest request on port number 8081
# CMD [ "python", "src/router/router/app.py" ]

#libraries to include

from flask import request, jsonify
from flask import Flask

import sys
sys.path.append('/Users/kripa.sharma/Desktop/my-local-git-repo/smart-gatted-society-db')
from src.controller.sg_controller import SecurityGuardController

# create app object
app = Flask(__name__)

@app.route('/sgsd/v1/internal/heartbeat', methods=['GET'])
def heartbeat():
    if request.method=='GET':
        info = {"msg":"working"}
        return jsonify(isError= False,message= "Success",statusCode= 200,data= info), 200
    else:
        return jsonify(isError= True,message= "Failed",statusCode= 404,data= ""), 200

@app.route('/sgsd/v1/internal/sg/register', methods=['POST'])
def sg_register():
    if request.method == 'POST':
        # start getting data from post json request
        content = request.json
        sg_id = content.get('sg_id')
        user_name = content.get('user_name')
        mobile_number =  content.get('mobile_number')
        email_id = content.get('email_id')
        password = content.get('password')
        is_approved = content.get('is_approved')

        info  = {'sg_id' : sg_id, 'user_name' : user_name, 'mobile_number': mobile_number,
        'email_id': email_id, 'password':password, 'is_approved':is_approved}

        # create object of controller
        sg = SecurityGuardController()
        response = sg.signUp(info)

        return jsonify(isError= False,message= "Success",statusCode= 200,data= response), 200




@app.route('/sgsd/v1/internal/sg/login', methods=['POST'])
def sg_login():
    if request.method == 'POST':
        pass

@app.route('/sgsd/v1/internal/sg/resetpassword', methods=['POST'])
def sg_reset_password():
    if request.method == 'POST':
        pass

@app.route('/sgsd/v1/internal/sg/logout', methods=['POST'])
def sg_logout():
    if request.method == 'POST':
        pass

@app.route('/sgsd/v1/internal/fw/register', methods=['POST'])
def fw_register():
    if request.method == 'POST':
        pass

@app.route('/sgsd/v1/internal/fw/login', methods=['POST'])
def fw_login():
    if request.method == 'POST':
        pass

@app.route('/sgsd/v1/internal/fw/resetpassword', methods=['POST'])
def fw_reset_password():
    if request.method == 'POST':
        pass

@app.route('/sgsd/v1/internal/fw/logout', methods=['POST'])
def fw_logout():
    if request.method == 'POST':
        pass

@app.route('/sgsd/v1/internal/societyadmin/register', methods=['POST'])
def society_admin_register():
    if request.method == 'POST':
        pass

@app.route('/sgsd/v1/internal/societyadmin/login', methods=['POST'])
def society_admin_login():
    if request.method == 'POST':
        pass

@app.route('/sgsd/v1/internal/societyadmin/resetpassword', methods=['POST'])
def society_admin_reset_password():
    if request.method == 'POST':
        pass

@app.route('/sgsd/v1/internal/societyadmin/logout', methods=['POST'])
def society_admin_logout():
    if request.method == 'POST':
        pass



"""
@app.route('/get/questions/', methods=['GET', 'POST','DELETE', 'PATCH'])
    def question():
    # request.args is to get urls arguments


    if request.method == 'GET':
        start = request.args.get('start', default=0, type=int)
        limit_url = request.args.get('limit', default=20, type=int)
        questions = mongo.db.questions.find().limit(limit_url).skip(start);
        data = [doc for doc in questions]
        return jsonify(isError= False,
                    message= "Success",
                    statusCode= 200,
                    data= data), 200

# request.form to get form parameter

    if request.method == 'POST':
        average_time = request.form.get('average_time')
        choices = request.form.get('choices')
        created_by = request.form.get('created_by')
        difficulty_level = request.form.get('difficulty_level')
        question = request.form.get('question')
        topics = request.form.get('topics')
"""

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8085)