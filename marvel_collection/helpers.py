from flask import request, jsonify, json
from functools import wraps
import secrets
import decimal

from marvel_collection.models import Character, User

def token_required(our_flask_function):
    @wraps(our_flask_function)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token'].split()[1]
            print(token)
        
        if not token:
            return jsonify({"message": "Token is missing!"}), 401
        
        try:
            current_user_token = User.query.filter_by(token = token).first() 
            print(current_user_token)
            if not current_user or current_user.token != token:
                return jsonify({"message": "Token is invalid"})
        
        except:
            current_user = User.query.filter_by(token = token).first()
            if token != current_user.token and secrets.compare_digest(token, current_user.token):
                return jsonify({"message": "Token is invalid"})
        return our_flask_function(current_user_token, *args, **kwargs)
    return decorated



class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        return super(JSONEncoder, self).default(obj)