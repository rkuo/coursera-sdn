#!/usr/bin/python

'''
Coursera:
- Software Defined Networking (SDN) course
-- Module 2 Programming Assignment
'''

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink

class CustomTopo(Topo):
    "Simple Data Center Topology"

    "linkopts - (1:core, 2:aggregation, 3: edge) parameters"
    "fanout - number of child switch per parent switch"
    def __init__(self, linkopts1, linkopts2, linkopts3, fanout=2, **opts):
        # Initialize topology and default options
        print "in class before init"
        Topo.__init__(self, **opts)
        print "in class after init"

        # Add your logic here ...
        """
        self.linkopts1 = linkopts1
        self.linkopts2 = linkopts2
        self.linkopts3 = linkopts3
        self.fanout = fanout
        """

        pfx = ['c', 'a', 'e', 'h']
        fo = [2, 2, 2, 0]
        lo = ['l1', 'l2', 'l3', '']


        # set part of node label = 1
        n_num = [0] * len(pfx)              # init for node label-numbering

        # create core
        n_num[0] += 1	    		        # node number
        c_node_name = pfx[0]+"%s" %n_num[0]
        print "core sw %s" %c_node_name
        self.addSwitch(c_node_name)

        for i in range(fanout):
            n_num[1] += 1	    		    # node number
            a_node_name = pfx[1]+"%s" %n_num[1]
            print "  aggr sw %s" %a_node_name
            self.addSwitch(a_node_name)

            print "    link %s - %s" %(c_node_name, a_node_name)
            self.addLink(c_node_name, a_node_name, **linkopts1)

            for j in range(fanout):
                n_num[2] += 1	    		# node number
                e_node_name = pfx[2]+"%s" %n_num[2]
                print "    edge sw %s" %e_node_name
                self.addSwitch(e_node_name)

                print "    link %s - %s" %(a_node_name, e_node_name)
                self.addLink(a_node_name, e_node_name, **linkopts2)

                for k in range(fanout):
                    n_num[3] += 1	    		# node number
                    h_node_name = pfx[3]+"%s" %n_num[3]
                    print "      host  %s" %h_node_name
                    self.addHost(h_node_name)
                    print "       link %s - %s" %(e_node_name, h_node_name)
                    self.addLink(e_node_name, h_node_name, **linkopts3)

topos = { 'custom': ( lambda: CustomTopo() ) }

if __name__ == '__main__':

    def simpleTest():
        linkopts1 = {'bw':50, 'delay':'5ms'}
        linkopts2 = {'bw':30, 'delay':'10ms'}
        linkopts3 = {'bw':10, 'delay':'15ms'}
        topo = CustomTopo(linkopts1, linkopts2, linkopts3, fanout=3)
        net = Mininet(topo=topo, link=TCLink)
        net.start()
        net.pingAll()
        print net.hosts
        print net.switches
        net.stop

    simpleTest()


