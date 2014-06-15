# Coursera SDN class wk-3 notes - 1

---
title: Coursera SDN class wk-3 notes - 1
tags: 
- Coursera
- SDN
---

This is the study notes for Coursera SDN class. I tried to follow the assignment instruction.

[TOC] 


**at 1st terminal on host:**

```
» ssh -X mininet@192.168.56.111
mininet@mininet-vm:~$ sudo mn --topo single,3 --mac --switch ovsk --controller remote
mininet> xterm h1 h2 h3
```
This will create 3 hosts, 1 switch and 1 controller in mininet-vm.

```
*** Creating network
*** Adding controller
Unable to contact the remote controller at 127.0.0.1:6633
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
mininet> xterm h1 h2 h3

```

if you ping each other, it will fail. 

**at 2nd terminal on host:**

» `ssh -X mininet@192.168.56.111`

### install hub

`mininet@mininet-vm:~$ pox.py log.level --DEBUG forwarding.hub`

```
POX 0.1.0 (betta) / Copyright 2011-2013 James McCauley, et al.
INFO:forwarding.hub:Hub running.
DEBUG:core:POX 0.1.0 (betta) going up...
DEBUG:core:Running on CPython (2.7.4/Apr 19 2013 18:28:01)
DEBUG:core:Platform is Linux-3.8.0-19-generic-x86_64-with-Ubuntu-13.04-raring
INFO:core:POX 0.1.0 (betta) is up.
DEBUG:openflow.of_01:Listening on 0.0.0.0:6633
INFO:openflow.of_01:[00-00-00-00-00-01 1] connected
INFO:forwarding.hub:Hubifying 00-00-00-00-00-01
```

**at h2 xterm on mininet vm:**

`root@mininet-vm:~# tcpdump -XX -n -i h2-eth0`


system replies;

```
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on h2-eth0, link-type EN10MB (Ethernet), capture size 65535 bytes
```

**at h3 xterm on mininet vm:**

`root@mininet-vm:~# tcpdump -XX -n -i h3-eth0`

system replies;

```
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on h3-eth0, link-type EN10MB (Ethernet), capture size 65535 bytes
```
### ping

**at h1 xterm on mininet vm:**

`root@mininet-vm:~# ping -c 1 10.0.0.2`

```
PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.
64 bytes from 10.0.0.2: icmp_req=1 ttl=64 time=0.712 ms
```

### response

**at 2nd terminal on host:**
reponse to ping:

```
03:43:39.681517 ARP, Request who-has 10.0.0.2 tell 10.0.0.1, length 28
        0x0000:  ffff ffff ffff 0000 0000 0001 0806 0001  ................
        0x0010:  0800 0604 0001 0000 0000 0001 0a00 0001  ................
        0x0020:  0000 0000 0000 0a00 0002                 ..........
03:43:39.681619 ARP, Reply 10.0.0.2 is-at 00:00:00:00:00:02, length 28
......
```

**at 3rd terminal on host:**
response to ping:

```
03:43:39.681502 ARP, Request who-has 10.0.0.2 tell 10.0.0.1, length 28
        0x0000:  ffff ffff ffff 0000 0000 0001 0806 0001  ................
        0x0010:  0800 0604 0001 0000 0000 0001 0a00 0001  ................
        0x0020:  0000 0000 0000 0a00 0002                 ..........
03:43:39.681812 ARP, Reply 10.0.0.2 is-at 00:00:00:00:00:02, length 28
......
```


**at h1 xterm on mininet vm:**
receives feedback;

```
--- 10.0.0.2 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.712/0.712/0.712/0.000 ms
```

On Mac, XQuartz needs to be updated for xterm to wark.




