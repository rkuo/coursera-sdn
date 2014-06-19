'''
Coursera:
- Software Defined Networking (SDN) course
-- Network Virtualization

Professor: Nick Feamster
Teaching Assistant: Arpit Gupta
'''

from pox.core import core
from collections import defaultdict

import pox.openflow.libopenflow_01 as of
import pox.openflow.discovery
import pox.openflow.spanning_tree

from pox.lib.revent import *
from pox.lib.util import dpid_to_str
from pox.lib.util import dpidToStr
from pox.lib.addresses import IPAddr, EthAddr
from collections import namedtuple
import os

log = core.getLogger()


class TopologySlice (EventMixin):

    def __init__(self):
        self.listenTo(core.openflow)
        log.debug("Enabling Slicing Module")        
        
    """This event will be raised each time a switch will connect to the controller"""
    def _handle_ConnectionUp(self, event):
        
        # Use dpid to differentiate between switches (datapath-id)
        # Each switch has its own flow table. As we'll see in this 
        # example we need to write different rules in different tables.
        dpid = dpidToStr(event.dpid)
        log.debug("Switch %s has come up.", dpid)
        
        """ Add your logic here """
        matchRule = of.ofp_match()
        fm = of.ofp_flow_mod()          # flow modification messagr
            
        if dpid == 1:       # s1
            log.debug("Setting rules for switch %d", dpid)
            matchRule.dl_src = EthAddr('00:00:00:00:00:03')     #s1 <- s3
            matchRule.dl_dst = EthAddr('00:00:00:00:00:01')     #s1
            fm.match = matchRule
            fm.actions.append(of.ofp_action_output(port = 1))
            event.connection.send(fm)

            matchRule.dl_src = EthAddr('00:00:00:00:00:01')     #s1 -> s3
            matchRule.dl_dst = EthAddr('00:00:00:00:00:03')     #s3
            fm.match = matchRule
            fm.actions.append(of.ofp_action_output(port = 3))
            event.connection.send(fm)

            """  different approach
            input_port = 1                      # -> s
            output_port = 3                     # s ->
            fm.match.input_port = input_port
            fm.match.output_port = output_port
            fm.actions.append(of.ofp_action_output(port = output_port))
            event.connection.send(fm)

            input_port = 3                      # -> s
            output_port = 1                     # s ->
            fm.match.input_port = input_port
            fm.match.output_port = output_port
            fm.actions.append(of.ofp_action_output(port = output_port))
            event.connection.send(fm)
            """
        
        if dpid == 4:       # s4
            pass
        if dpid == 2:       # s2
            pass
        if dpid == 3:       # s3
            pass

def launch():
    # Run spanning tree so that we can deal with topologies with loops
    pox.openflow.discovery.launch()
    pox.openflow.spanning_tree.launch()

    '''
    Starting the Topology Slicing module
    '''
    core.registerNew(TopologySlice)
