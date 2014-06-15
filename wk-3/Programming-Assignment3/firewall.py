#!/usr/bin/python

'''
Coursera:
- Software Defined Networking (SDN) course
-- Programming Assignment: Layer-2 Firewall Application

Professor: Nick Feamster
Teaching Assistant: Arpit Gupta
'''

from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr
from collections import namedtuple
import os

''' Add your imports here ... '''

import csv

log = core.getLogger()
policyFile = "%s/pox/pox/misc/firewall-policies.csv" % os.environ[ 'HOME' ]  

''' Add your global variables here ... '''
policyTable = []

with open(policyFile, 'rb') as f:
    csv_entry = csv.reader(f, delimiter=',')
    for row in csv_entry:
	# --> ['1', '00:00:00:00:00:01', '00:00:00:00:00:02'] []
        log.debug("row data from csv file %s ", row)
	policyTable.append(row[1:])

    for rule in policyTable:	
        # --> ['00:00:00:00:00:01', '00:00:00:00:00:02'] []
	log.debug("rules are %s", rule)

class Firewall (EventMixin):

    def __init__ (self):
        self.listenTo(core.openflow)
        log.debug("Enabling Firewall Module")

    def _handle_ConnectionUp (self, event):    
        ''' Add your logic here ... '''
        for rule in policyTable:
            my_match = of.ofp_match()
            my_match.dl_src = EthAddr(rule[0])
            my_match.dl_dst = EthAddr(rule[1])
	    # construct flow modify message 
            msg = of.ofp_flow_mod()
            msg.match = my_match
            event.connection.send(msg)
    
        log.debug("Firewall rules installed on %s", dpidToStr(event.dpid))

def launch ():
    '''
    Starting the Firewall module
    '''
    core.registerNew(Firewall)

