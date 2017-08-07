#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime
import bitso
import sqlite3 as lite
import sys

api = bitso.Api()

books = api.available_books()
books

time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print time

btc_mxn = api.ticker('btc_mxn')
eth_mxn = api.ticker('eth_mxn')
xrp_btc = api.ticker('xrp_btc')
xrp_mxn = api.ticker('xrp_mxn')
eth_btc = api.ticker('eth_btc')
bch_btc = api.ticker('bch_btc')

con = lite.connect('./Database/bitso.db')

with con:

    cur = con.cursor()
    query = "INSERT INTO bitso_daily (Date, btc_mxn_ask, btc_mxn_bid, btc_mxn_high, btc_mxn_last, btc_mxn_low, btc_mxn_vmaplow, eth_btc_ask, eth_btc_bid, eth_btc_high, eth_btc_last, eth_btc_low, eth_btc_vmaplow, eth_mxn_ask, eth_mxn_bid, eth_mxn_high, eth_mxn_last, eth_mxn_low, eth_mxn_vmaplow, bch_btc_ask, bch_btc_bid, bch_btc_high, bch_btc_last, bch_btc_low, bch_btc_vmaplow, xrp_btc_ask, xrp_btc_bid, xrp_btc_high, xrp_btc_last, xrp_btc_low, xrp_btc_vmaplow, xrp_mxn_ask, xrp_mxn_bid, xrp_mxn_high, xrp_mxn_last, xrp_mxn_low, xrp_mxn_vmaplow) VALUES('%s', %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f)" % (time, btc_mxn_maximum_amount, btc_mxn_maximum_price, btc_mxn_maximum_value, btc_mxn_minimum_amount, btc_mxn_minimum_price, btc_mxn_minimum_value, eth_btc_maximum_amount, eth_btc_maximum_price, eth_btc_maximum_value, eth_btc_minimum_amount, eth_btc_minimum_price, eth_btc_minimum_value, eth_mxn_maximum_amount, eth_mxn_maximum_price, eth_mxn_maximum_value, eth_mxn_minimum_amount, eth_mxn_minimum_price, eth_mxn_minimum_value, xrp_btc_maximum_amount, xrp_btc_maximum_price, xrp_btc_maximum_value, xrp_btc_minimum_amount, xrp_btc_minimum_price, xrp_btc_minimum_value, xrp_mxn_maximum_amount, xrp_mxn_maximum_price, xrp_mxn_maximum_value, xrp_mxn_minimum_amount, xrp_mxn_minimum_price, xrp_mxn_minimum_value)
    print query
    cur.execute(query)

if con:
    con.close()
