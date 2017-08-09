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

#Database Operations
with con:

    cur = con.cursor()
    query = "INSERT INTO bitso_daily (Date, btc_mxn_ask, btc_mxn_bid, btc_mxn_high, btc_mxn_last, btc_mxn_low, btc_mxn_vmaplow, eth_btc_ask, eth_btc_bid, eth_btc_high, eth_btc_last, eth_btc_low, eth_btc_vmaplow, eth_mxn_ask, eth_mxn_bid, eth_mxn_high, eth_mxn_last, eth_mxn_low, eth_mxn_vmaplow, bch_btc_ask, bch_btc_bid, bch_btc_high, bch_btc_last, bch_btc_low, bch_btc_vmaplow, xrp_btc_ask, xrp_btc_bid, xrp_btc_high, xrp_btc_last, xrp_btc_low, xrp_btc_vmaplow, xrp_mxn_ask, xrp_mxn_bid, xrp_mxn_high, xrp_mxn_last, xrp_mxn_low, xrp_mxn_vmaplow) VALUES('%s', %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f)" % (time, btc_mxn.ask, btc_mxn.bid, btc_mxn.high, btc_mxn.last, btc_mxn.low, btc_mxn.vwap, eth_btc.ask, eth_btc.bid, eth_btc.high, eth_btc.last, eth_btc.low, eth_btc.vwap, eth_mxn.ask, eth_mxn.bid, eth_mxn.high, eth_mxn.last, eth_mxn.low, eth_mxn.vwap, bch_btc.ask, bch_btc.bid, bch_btc.high, bch_btc.last, bch_btc.low, bch_btc.vwap, xrp_btc.ask, xrp_btc.bid, xrp_btc.high, xrp_btc.last, xrp_btc.low, xrp_btc.vwap, xrp_mxn.ask, xrp_mxn.bid, xrp_mxn.high, xrp_mxn.last, xrp_mxn.low, xrp_mxn.vwap)
    #print query
    cur.execute(query)

if con:
    con.close()
