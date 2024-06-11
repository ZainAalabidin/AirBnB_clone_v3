##!/usr/bin/python3
#"""
#Create a new view for State objects
#that handles all default RESTFul API actions
#"""
#from flask import Flask, jsonify, make_response, request, abort
#from api.v1.views import app_views
#from models import storage
#from models.state import State
#import json
#
#
#@app_views.route("/states", methods=["GET"], strict_slashes=False)
#def get_states():
#    """
#    Retrieves the list of all State objects
#    """
#    all_states = storage.all(State).values()
#    states_list = [state.to_dict() for state in all_states]
#    response = make_response(json.dumps(states_list, indent=2) + "\n")
#    response.headers["Content-Type"] = "application/json"
#    return response
#
#
#@app_views.route("/states/<state_id>", methods=["GET"], strict_slashes=False)
#def get_state(state_id):
#    """Retrieves a State object by id"""
#    state = storage.get(State, state_id)
#    if not state:
#        abort(404)
#    response = make_response(json.dumps(state.to_dict(), indent=2) + "\n")
#    response.headers["Content-Type"] = "application/json"
#    return response
#
#
#@app_views.route("/states/<state_id>", methods=["DELETE"], strict_slashes=False)
#def delete_state(state_id):
#    """Deletes a State object"""
#    state = storage.get(State, state_id)
#    if not state:
#        abort(404)
#    storage.delete(state)
#    storage.save()
#    return make_response(jsonify({}), 200)
#
#
#@app_views.route("/states", methods=["POST"], strict_slashes=False)
#def create_state():
#    """create state use POST request"""
#    if not request.get_json():
#        abort(400, description="Not a JSON")
#    if "name" not in request.get_json():
#        abort(400, description="Missing name")
#
#    data = request.get_json()
#    instance = State(**data)
#    instance.save()
#    response = make_response(json.dumps(instance.to_dict(), indent=2) + "\n")
#    response.headers["Content-Type"] = "application/json"
#    return response, 201
#
#
#@app_views.route("/states/<state_id>", methods=["PUT"], strict_slashes=False)
#def updata_state(state_id):
#    """update state"""
#    state = storage.get(State, state_id)
#    if not state:
#        abort(404)
#    if not request.get_json():
#        abort(400, description="Not a JSON")
#    data = request.get_json()
#    for k, v in data.items():
#        if k not in ["id", "created_at", "updated_at"]:
#            setattr(state, k, v)
#
#    storage.save()
#    response = make_response(json.dumps(state.to_dict(), indent=2) + "\n")
#    response.headers["Content_Type"] = "application/json"
#    return response, 200
#