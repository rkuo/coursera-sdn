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
        match_rule = of.ofp_match()
        flow_msg = of.ofp_flow_mod()        # flow messagr for modification

        """ 
        # option-1 use src/dst Mac addresses to do matching, but in_port is easier
            forwardRule.dl_src = EthAddr("00:00:00:00:00:01")
            forwardRule.dl_dst = EthAddr("00:00:00:00:00:03")
        """
       
        # option-2 simplify the code later with this function
        def getFlowMsg(in_port, out_port):
            msg = of.ofp_flow_mod()    # flow messagr for modification
            msg.match.in_port = in_port
            msg.actions.append(of.ofp_action_output(port = out_port))

            return msg     
            # this is equivalent to fm_s1s4p13, ... below, may not needed

        if dpid == '00-00-00-00-00-01' or dpid == '00-00-00-00-00-04':
            log.debug("Setting rules for switch %d", dpid)

            # upper flow
            in_port = 1                     
            out_port = 3                    
            event.connection.send(getFlowMsg(in_port, out_port))

            in_port = 3                     
            out_port = 1                    
            event.connection.send(getFlowMsg(in_port, out_port))

            # upper flow
            in_port = 2                     
            out_port = 4                    
            event.connection.send(getFlowMsg(in_port, out_port))

            in_port = 4                    
            out_port = 2                   
            event.connection.send(getFlowMsg(in_port, out_port))

        elif dpid == '00-00-00-00-00-02' or dpid == '00-00-00-00-00-03':
            
            in_port = 1
            out_port = 2            
            event.connection.send(getFlowMsg(in_port, out_port))
            
            in_port = 2
            out_port = 1
            event.connection.send(getFlowMsg(in_port, out_port))

""" delete this testing code between marks """
def test():

    print "a. Firing up Mininet"
    #setLogLevel('info')
    topo = FVTopo()          
    net = Mininet( topo=topo, link = TCLink, controller=TopologySliceController, autoSetMacs=True )

    net.start()
    time.sleep(1)

    print "b. Starting Test"
    # Start pings
    outputString = str(net.pingAll())
    print "The output string is: ",outputString


    print "c. Stopping Mininet"
    net.stop()

# TODO: Used for tests. Uncomment to test locally.
if __name__ == '__main__':
    setLogLevel('info')
    test()

""" delete this testing code between marks """

        
def launch():
    # Run spanning tree so that we can deal with topologies with loops
    pox.openflow.discovery.launch()
    pox.openflow.spanning_tree.launch()

    '''
    Starting the Topology Slicing module
    '''
    core.registerNew(TopologySlice)
