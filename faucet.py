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

def wow():
    balance = b.get_balance()['data']['available_balance']
    return balance

def such():
    donation_address = b.get_my_addresses()['data']['addresses'][0]['address']
    app.logger.info('address='+donation_address)
    return donation_address

@app.route("/", methods=['GET','POST'] )
def home():
    if request.method == 'POST':
        requested_address = request.form['address']
    else:
        requested_address = ''
    return render_template('home.html', requested_address=requested_address, balance=wow(), donation_address=such() )

if __name__ == '__main__':
    app.run()
