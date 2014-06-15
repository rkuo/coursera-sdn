# coursera SDN wk-3 notes

As skelton code indicates, there are 3 places require coding:

1. get csv data in, 
2. write logic/rules and 
3. start the program.

## Homework Preparation

Needs to read the documents for pox and all libraries list on import statements.

```
from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr
from collections import namedtuple
import os
```

- [pox document](https://openflow.stanford.edu/display/ONL/POX+Wiki)
- [Revent](http://www.noxathome.org/doc/pox/pox.lib.revent.revent.html)
- [event driven programming](http://collection.openlibra.com.s3.amazonaws.com/pdf/event_driven_programming.pdf?AWSAccessKeyId=AKIAIGY5Y2YOT7GYM5UQ&Signature=Mge%2BoH6OGG2gF83ggyi1V8oexm4%3D&Expires=1402783396)
- [What is the difference between event driven model and reactor pattern?](http://stackoverflow.com/questions/9138294/what-is-the-difference-between-event-driven-model-and-reactor-pattern)
- [learning from example - Convert pox/pox/misc/of_tutorial.py]()

### Launch the code
From [sdn-hub pox](http://sdnhub.org/tutorials/pox/):
Launch is the main for the app, which will register the new object, and eventlisterners. So, in a way, our code is to 
- define listener(s) to listen a set of events and 
- follow defined logic/rules, which can be external: configuration files, csv,etc
- take action(s)


### CSV file

We need to read/open a csv file.
- find a the library to import.
- the statement for read or open.
- the option of delimiter.
- loop thru the csv file and parse the line to different varibles.

From the policy file, there are 3 variables,
The line one is column header,
id, src_mac_address and dst_mac_address

see [code recommendation](http://stackoverflow.com/questions/5757743/python-how-can-i-get-a-specific-field-of-a-csv-file)

```
policyTable = []

with open(policyFile) as f:
    next(f)
    csv_entry = csv.reader(f, delimiter=',')
    for row in csv_entry:
        policyTable.append(row[1:])
```

The rest lines are data. Since it is a list, we can get the data by index. 

### Code

OpenFlow (of) defines a [match structure](defines https://openflow.stanford.edu/display/ONL/POX+Wiki#POXWiki-MatchStructure) to against headers. If it matchs the conditions, some actions can be taken, i.e. send out message.

```
my_match = of.ofp_match(in_port = 5, dl_dst = EthAddr("01:02:03:04:05:06"))
my_match.dl_dst = EthAddr("01:02:03:04:05:06")
```

For wk-3 homework, if two dl addresses (dl_src and dl_dst) match --> [modify flow table](https://openflow.stanford.edu/display/ONL/POX+Wiki#POXWiki-ofp_flow_mod-Flowtablemodification).

Then send modification message to switch.

### Compile

"Use exit() or Ctrl-D (i.e. EOF) to exit POX".
Got error message "error: [Errno 98] Address already in use"
Either send `sudo fuser -k 6633/tcp` in mininet to kill exist process or add `os.popen("fuser -k 6633/tcp") ` in your code. 

### Test code
We will test our code with, `pox.py forwarding.l2_learning misc.firewall`
This runs two python programs without py extension. Since firewall.py is in misc directory, assume, l2_learning is in forwarding directory. checked, ok.

Review submit.py, to see what is expected.

```
def output(partIdx):
  """Uses the student code to compute the output for test cases."""
  outputString = ''
  
  if partIdx == 0: # This is m4a
    print "a. Firing up Mininet"
    net = Mininet( topo=SingleSwitchTopo( 8 ), controller=POXBridge, autoSetMacs=True )                                  
    net.start()   

    h3 = net.get('h3')
    h4 = net.get('h4')
    h6 = net.get('h6')
  
    print "b. Starting Test"
    # Start pings
    outputString += h3.cmd('ping', '-c3', h6.IP())
    outputString += h4.cmd('ping', '-c3', h6.IP())

    print outputString
    
    print "c. Stopping Mininet"
    net.stop()
    
  return outputString.strip()
```
Follow the assignment instruction; works.

```
mininet@mininet-vm:~$ sudo mn --topo single,3 --controller remote --mac
*** Creating network
*** Adding controller
*** Adding hosts:
h1 h2 h3
*** Adding switches:
s1
*** Adding links:
(h1, s1) (h2, s1) (h3, s1)
*** Configuring hosts
h1 h2 h3
*** Starting controller
*** Starting 1 switches
s1
*** Starting CLI:
mininet> h1 ping -c 1 h2
PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.

--- 10.0.0.2 ping statistics ---
1 packets transmitted, 0 received, 100% packet loss, time 0ms

mininet> h1 ping -c 1 h3
PING 10.0.0.3 (10.0.0.3) 56(84) bytes of data.
64 bytes from 10.0.0.3: icmp_req=1 ttl=64 time=6.20 ms

--- 10.0.0.3 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 6.205/6.205/6.205/0.000 ms
mininet>
```

