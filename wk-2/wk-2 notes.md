# Coursera - SDN week 2

## To do 
- setup all codes in github and doc in dropbox (should be in one place).
- test mininet installation, 
	- get IP of eth1 of mininet VM within mininet VM: `sudo dhclient eth1` and `ifconfig eth1` -> 192.168.56.101
	- I had problem of login the vm, followed the instruction from this [link](https://forums.virtualbox.org/viewtopic.php?f=8&t=59354), worked. 
	- start a new console/iterm2, and login mininet VM, `ssh -X mininet@192.168.56.101`
	- test mininet installation `sudo mn --test pingall --topo single,3`. Note-there is no space before 3. works!
	- get out of mininet `exit` and clean up `mn -c`
	- setup clipboard sharing (in VirtualBox console, Devices -> Shared clipboard -> bidirectional) and setup file directory sharing between VM and host. In order to share folder, we need to install guestAdditions first, follow this [instruction](http://en.ig.ma/notebook/2012/virtualbox-guest-additions-on-ubuntu-server). Then, in Virtualbox console -> Devices -> Shared Directory Setup -> plus sign to add, select the directroy on host to share.
	- reboot the VM.
	- shared folder is in `/media/sf_sdn` which we can locate our python code in `coursera-sdn/wk-2` There is a [online instruction](http://www.ubuntugeek.com/how-to-access-windows-host-shared-folders-from-ubuntu-guest-in-virtualbox.html)
	- workflow: use host project directory for all homework, then run python file for creating mininet network. You can use the tools on your host (i.e. versioning, editor, ..) for development.

## Video
- Module 2.2 slide-10 Mac address can be reassigned?
- RCP replicates see the same information to do the same calculation. Each function is implemented with a cluster. For example to use `CoreOS` for cluster, and use `etcd` to ensure the consistency. *Recommendation: study distributed computing.*
- Module 2.4 efficient aggregation uses sub-addressing.
- Module 2.5 can I say, SDN combines management layer and control layer together. 
- Network goals, views, direct control. 4D - Decision, Dissemination, Discovery and Data. Very good slide on time[7:00-7:20] 
	- Data: for processing packets
	- Discovery: for collecting topology and traffic
	- Dissemination: installing packet-processing rules
	- Decision: logically centralizing controllers convert objectives into packet-handling state.
- [Interview with David Clark](https://class.coursera.org/sdn-002/lecture/25): 
	- old thinking - control follows data flow,
	
- presentation from [Stanford NetSeminar - Teemu Koponen (Nicira/VMware)](https://www.youtube.com/watch?v=bx0XCjJQt70) Watch [Netseminar](http://netseminar.stanford.edu/)

## Resources
- [OpenFlow Tutorial](http://archive.openflow.org/wk/index.php/OpenFlow_Tutorial)
- [Mininet walkthrough](http://mininet.org/walkthrough/)

## Quiz
- Read [Mininet walkthrough](http://mininet.org/walkthrough/) and [mininet test instruction](https://class.coursera.org/sdn-002/wiki/Mininet_Quiz_Instructions) before taking the quiz-2.


## Homework
- build datacenter with multiple layers tree structure. 
- topology is all about switch.
- [Dictionary Manipulation in Python](http://www.pythonforbeginners.com/dictionary/dictionary-manipulation-in-python)	
- 
	


