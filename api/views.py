from flask import Flask, jsonify, request, json
from api.models import Incident
import datetime

app = Flask(__name__)

incident_list = []

@app.route('/')
def index():
    return "Welcome"

    
@app.route('/api/v1/red-flags', methods=['POST'])
def create_flag():

    data = request.get_json()
    flag_id = len(incident_list) + 1
    created_by = data['created_by']
    created_on = datetime.datetime.now()
    incident_type = data['incident_type']
    location = data['location']
    comment = data['comment']
    images = data['images']
    videos = data['videos']

    redflag = Incident(flag_id, created_by, created_on, incident_type, location, comment, images, videos)
   
    incident_list.append(redflag.__dict__)
    return jsonify({
    'status': 201,
    'message': 'created redflag reccord!',
    'id': flag_id,
    'data': redflag.__dict__
       }), 201

    
   

@app.route('/api/v1/red-flags/all', methods=['GET'])
def get_flags():

    return jsonify({"status":200, "data": incident_list})
    

@app.route('/api/v1/red-flags/<int:red_flag_id>', methods=['GET'])
def get_specific_flag(red_flag_id):

    red_flag_by_id = [redflag for redflag in incident_list if redflag['flag_id']== red_flag_id]
    return jsonify({"status":200, "data":red_flag_by_id})

   

@app.route('/api/v1/red-flags/<int:red_flag_id>/location', methods=['PATCH'])
def edit_flag_location(red_flag_id):
    data = request.get_json()
    new_location = data['location']
    red_flag_to_change_location = [redflag for redflag in incident_list if redflag['flag_id']== red_flag_id]
    red_flag_to_change_location[0]['location'] = new_location
    return jsonify({
    "status":200, 
    "message":"Edit successful",
    "data":red_flag_to_change_location })



@app.route('/api/v1/red-flags/<int:red_flag_id>/comment', methods=['PATCH'])
def edit_flag_comment(red_flag_id):
    data = request.get_json()
    new_comment = data['comment']
    red_flag_to_change_comment = [redflag for redflag in incident_list if redflag['flag_id']== red_flag_id]
    red_flag_to_change_comment[0]['comment'] = new_comment
    return jsonify({"status":200,"incident": red_flag_to_change_comment})
   

@app.route('/api/v1/red-flags/<int:red_flag_id>', methods=['DELETE'])
def delete_red_flag(red_flag_id):

    completed_redflag = [redflag for redflag in incident_list if redflag['flag_id']== red_flag_id]
    incident_list.remove(completed_redflag[0])
    return jsonify({"status":200, "data":incident_list})   




if __name__ == '__main__':
    app.run(debug=True)