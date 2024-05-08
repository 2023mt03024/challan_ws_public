"""Module providing REST API for generating challan."""
import os
import json
import boto3
from boto3.dynamodb.conditions import Attr
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
        
# Create Flask app
app = Flask(__name__)

# about page
@app.route('/about')
def about():
    """ Function that show application information."""
    
    # Render the page with application information
    return render_template('about.html')

# index page
@app.route('/', methods=('GET', 'POST'))
def index():
    """ Function that allows to  generate a challan."""
    # Check for POST method
    if request.method == 'POST':
        # Vehicle Number is mandatory
        if not request.form['vehicle_number']:
            flash('Vehicle Number is required!')

        else: 
            # Get the challans for the specified vehicle
            response = tableChallans.scan(FilterExpression=Attr('Vehicle Number').eq(request.form['vehicle_number']))

            # Render index page
            return render_template('index.html', challans = response['Items'])

    # Render index page
    return render_template('index.html', challans = None)

# Starts from here
if __name__ == "__main__":   
        # Get endpoint url
	endpointUrl = endpoint_url='http://{}:{}'.format( 
                              os.getenv('DYNAMODB_SERVICE_HOST'),
                              os.getenv('DYNAMODB_SERVICE_PORT'))
      
    # Get dynamodb resource
	dynamodb = boto3.resource('dynamodb',  aws_access_key_id="anything", aws_secret_access_key="anything",
                          region_name="us-west-2", endpoint_url=endpointUrl)
          
    # Get Challans table
	tableChallans = dynamodb.Table('Challans')
     
    # Set the configuration
	app.config[os.getenv("FLASK_KEY")] = os.getenv("FLASK_KEY_VALUE")

    # Run the application
	app.run(host='0.0.0.0', port=8004)