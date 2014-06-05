'''
Coursera:
- Software Defined Networking (SDN) course
-- Programming Assignment 2

Professor: Nick Feamster
Teaching Assistant: Arpit Gupta, Muhammad Shahbaz
'''

from mininet.topo import Topo

class CustomTopo(Topo):
    "Simple Data Center Topology"

    "linkopts - (1:core, 2:aggregation, 3: edge) parameters"
    "fanout - number of child switch per parent switch"
    def __init__(self, linkopts1, linkopts2, linkopts3, fanout=2, **opts):
        # Initialize topology and default options
        Topo.__init__(self, **opts)
        
        # Add your logic here ...

# need testing code here
def simpleTest():
	# create and test simple network
	# bw is in mps, delay is in ms or us, loss is in percentag, 
	linkopts1 = {'bw': 30, 'delay': '20ms'}
	linkopts2 = {'bw': 20, 'delay': '10ms'}
	linkopts3 = {'bw': 10, 'delay': '10ms'}
	fanout = 2
	
	topo = CustomTopo(self, linkopts1, linkopts2, linkopts3, fanout=2, **opts)


# need this code for running local
if __name__ == 'main':
	# tell mininet to print useful information
	setLogLevel('info')
	simpleTest()
        
# this will be used for running on command line, unblock it for submit.py                    
# topos = { 'custom': ( lambda: CustomTopo() ) }