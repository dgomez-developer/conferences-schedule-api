import os
import json
import bottle
from bottle import route, run, template, request, post, BaseResponse, response

# the decorator
def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        # set CORS headers
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

        if bottle.request.method != 'OPTIONS':
            # actual request; reply with the actual response
            return fn(*args, **kwargs)

    return _enable_cors


app = bottle.app()

@app.route('/api/<conference>/schedule/<year>', method=['OPTIONS','GET'])
@enable_cors
def getConferenceSchedule(conference,year):
    response.content_type = 'application/json; charset=utf-8'
    body = open(conference + '/'+ year + '/schedule.json')
    return BaseResponse(body, 200, None)

run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
