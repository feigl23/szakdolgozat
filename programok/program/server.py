import json
import os
import sys

import falcon
import waitress

next_user_id = 0
world = {}


class LoginResource():

    def on_post(self, req, resp):
        global next_user_id
        data = json.loads(req.stream.read().decode('utf-8'))
        message = {'user_id': next_user_id}
        next_user_id += 1
        resp.body = json.dumps(message)
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_200


class WorldResource():

    def on_get(self, req, resp):
        resp.body = json.dumps(world)
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_200

    def on_put(self, req, resp):
        global world
        world = json.loads(req.stream.read().decode('utf-8'))
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_200


app = falcon.API()

login_resource = LoginResource()
world_resource = WorldResource()

app.add_route('/api/login', login_resource)
app.add_route('/api/world', world_resource)

waitress.serve(app, host='0.0.0.0', port=5000)
