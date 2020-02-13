import os
import json
from bottle import route, run, template, request, post, BaseResponse, response

@route('/api/<conference>/schedule/<year>')
def getConferenceSchedule(conference,year):
    response.content_type = 'application/json; charset=utf-8'
    body = open(conference + '/'+ year + '/schedule.json')
    return BaseResponse(body, 200, None)

run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
