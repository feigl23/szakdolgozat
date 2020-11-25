import json

import requests

class Requests:

    def require_user_id(self):
        """
        Require the user identifier from the server.
        """
        credential = {}
        resp = requests.post('http://0.0.0.0:5000/api/login', json=credential)
        user_id = resp.json()['user_id']
        return user_id


    def require_world_state(self):
        """
        Require the state of the virtual world.
        """
        resp = requests.get('http://0.0.0.0:5000/api/world')
        return resp.json()


    def upload_world_changes(self,world):
        """
        Upload the changed part of the virtual world.
        """
        resp = requests.put('http://0.0.0.0:5000/api/world', json=world)
