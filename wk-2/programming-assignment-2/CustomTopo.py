#!/usr/bin/python

pfx = ['c', 'a', 'e', 'h']
fo = [2, 2, 2, 0]
lo = ['l1', 'l2', 'l3', '']


# set part of node label = 1
csw_num = asw_num = esw_num = host_num = 1

# create core
pn = pfx[0]					# parent node
node_name = "c%s" %csw_num	# if more core sw; csw_num += 1
print node_name
# create core sw
# node = self.addSwitch(node_name)

p_node = node_name

for i in range(fo[0]):
    node_name = "a%s" %asw_num
    print node_name; asw_num += 1
    # create a sw
    # node = self.addSwitch(node_name)

    print p_node + " - " + node_name            # makelink
    p_node = node_name

    for j in range(fo[1]):
        node_name = "e%s" %esw_num;
        print node_name; esw_num += 1
        # create a sw
        # node = self.addSwitch(node_name)
        print p_node + " - " + node_name
        p_node = node_name

        for k in range(fo[2]):
            node_name = "h%s" %(host_num)
            print node_name; host_num += 1
            # create host
            # node = self.addHost(node_name)
            print p_node + " - " + node_name



