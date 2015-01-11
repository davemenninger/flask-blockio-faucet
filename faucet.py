#!/usr/bin/env python

import os

from flask import Flask, render_template, request
app = Flask(__name__)
app.debug = True

import logging
from logging import StreamHandler
file_handler = StreamHandler()
app.logger.setLevel(logging.DEBUG)  # set the desired logging level here
app.logger.addHandler(file_handler)

app.logger.info("faucet is restarting")

# TODO: catch KeyError
apikey = os.environ['BLOCKIO_APIKEY']
secretpin = os.environ['BLOCKIO_SECRETPIN']

from block_io import BlockIo
version = 2
b = BlockIo(apikey,secretpin,version)

import requests

def wow():
    balance = b.get_balance()['data']['available_balance']
    return balance

def such():
    donation_address = b.get_my_addresses()['data']['addresses'][0]['address']
    return donation_address

def very(address):
    response = requests.get('https://chain.so/api/v2/is_address_valid/DOGE/'+address)
    if response.status_code == 200:
        content = response.json()
        return content['data']['is_valid']
    else:
        return False

@app.route("/", methods=['GET','POST'] )
def home():
    if request.method == 'POST':
        requested_address = request.form['address']
        if very(requested_address):
            is_request_good = True
            message = 'The address is good.'
        else:
            is_request_good = False
            message = 'The address is not good.'
    else:
        is_request_good = False
        requested_address = ''
        message = 'Input an address.'
    return render_template('home.html',
            is_request_good=is_request_good,
            requested_address=requested_address,
            message=message,
            balance=wow(),
            donation_address=such() )

if __name__ == '__main__':
    app.run()
