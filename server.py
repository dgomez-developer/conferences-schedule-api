import os
import json
from bottle import route, run, template, request, post, BaseResponse, response

@route('/api/<conference>/schedule/<year>')
def getConferenceSchedule(conference,year):
    return open(conference + '/'+ year + '/schedule.json')

run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
