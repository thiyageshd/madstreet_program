from flask import request
import requests
app = Flast(__name__)

import json, datetime


date = str(datetime.datetime.today().date())

product_dict = {

	date : {
		'ab1' : {
			'dateadded' : datetime.datetime.now() + datetime.timedelta(hours=1),
			'color' : 'yellow'
			},
		'ab2' : {
			'dateadded' : datetime.datetime.now() + datetime.timedelta(hours=-1),
			'color' : 'green'
			},
		'ab3' : {
			'dateadded' : datetime.datetime.now() + datetime.timedelta(hours=-1),
			'color' : 'pink'
			},
		'ab4' : {
			'dateadded' : datetime.datetime.now() + datetime.timedelta(hours=-2),
			'color' : 'yellow'
			},
			}
		}

@app.route('/getRecentItem', methods = ['GET'])
def get():
	data = request.data
    dateStr = str(datetime.datetime.today().date())
    productdict_data = product_dict.get(dateStr)
    for product, details in productdict_data.iteritems:
        recentProduct = product
        recentDate = details['dateadded']
        for date, color in details.iteritems:
            if date >= recentDate:
                recentDate = date
                recentProduct = product
    return json.dumps({'recentProductadded' : product})

	return json.dumps()

def main():
	app.run()