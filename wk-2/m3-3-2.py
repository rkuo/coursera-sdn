from mininet.net import Mininet
from mininet.topo import Topo

net = Mininet()

# creating nodes in network
c0 = net.addController()
s0 = net.addSwitch('s0')
h0 = net.addHost('h0')
h1 = net.addHost('h1')

# Creating links between nodes in network (2-ways)
net.addLink(h0, s0)
net.addLink(h1, s0)

# Configuration of IP addresses in interfaces
h0.setIP('192.168.1.1', 24)
h1.setIP('192.168.1.2', 24)

net.start()
net.pingAll()
# mininet.cli.CLI(net)
net.stop()
