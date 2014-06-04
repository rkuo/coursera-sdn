# Functional Programming in Python

I am trying to use FP for my Coursera-SDN class, which uses Python as main programming language for the class.

I need to learn some collections first, so I can apply functions to a collection. 

[TOC]

## Collection
The first collection is range, this allows me eventually avoid using loop.

### range
```
>>> r = range(10, 20, 3)
>>> 11 in r
False
>>> r[3]
19
```

There are [different constructors: irange, xrange, range.](http://stackoverflow.com/questions/22971078/how-is-irange-any-different-from-range-or-xrange)

For Python-2.7+, use range, which has some nice methods. 

```
>>> k = 3
>>> for i in range(0,k):\
... print i
...
0
1
2
```


Make it a label/key for something with this approach. For k = 3, 

```
>>> for i in range(0,k):\
... print ('h%s' %i)
...
h0
h1
h2
```

We can create host/switch name for mininet. 

### Dictionary
We need some thing to represent a tree, the best will be graph. But let's use Dictionary for now, which is a name of data structure, not a class name. In Python, it happens is a class. 

link: http://docs.python.org/tutorial/datastructures.html#dictionaries
"It is best to think of a dictionary as an unordered set of key: value pairs, with the requirement that the keys are unique..."

Python is not typed, type is inferred from its syntax:

```
dict = { 0: [1, 2], 1: [3], 2: [6], 3: [4,7], 'a': [5,8], 8: [9] }
print dict['a'][1]
```

This return the value at key= 'a' and value is a list, index = 1 (second position).

[Dictionary Manipulation in Python](http://www.pythonforbeginners.com/dictionary/dictionary-manipulation-in-python)

[Python Dictionary Quick Guide](http://www.pythonforbeginners.com/dictionary/python-dictionary-quick-guide)

```
dict = { 0: [1, 2], 'b': {'x': 4, 'y':5}, 2: [6], 3: [4,7], 'a': [5,8], 8: [9] }
print dict['b']['x']
```
We can mix list and dictionary as value in our data type. In this case, return value = 4.

Option is to use TreeDict, which requires key and value are String. The benefit is we can use b1.b2.x to get branch 1, sub-branch 2's x value. Heading that direction. 
[TreeDict](http://www.stat.washington.edu/~hoytak/code/treedict/overview.html)

I need to find a flexible way to have multiple branch and multiple depth dictionary and eventually connect to json data. 

```
dict = { 'a': {'s1': 1}, 'b': {'x': {'l': 9, 'm': 7}, 'y':5}, 'c': { 'x': 6}}
print dict['b']['y']
print dict['b']['x']
```

This will give us

```
5
{'l': 9, 'm': 7}
```

Since Dictionary can have Dictionary, let's try to see how to [use defaultdict](http://recursive-labs.com/blog/2012/05/31/one-line-python-tree-explained/) and [one line tree Python](https://gist.github.com/hrldcpr/2012250) like it suggested:

```
def tree(): 
	return defaultdict(tree)
```

Use the defined tree:

```
from collections import defaultdict

def tree(): 
    return defaultdict(tree)

core = tree()		# data_center
core['a1']['username'] = 'hrldcpr'
core['a2']['username'] = 'matthandlersux'

print core['a1']
print core['a1']['username']
```

This will return

```
defaultdict(<function tree>, {'username': 'hrldcpr'})
hrldcpr
```

Continue morph to our target;

```
from collections import defaultdict

def tree(): 
    return defaultdict(tree)

c1 = tree()		# data_center
c1 = {'a1' : {'e1':{}, 'e2':{}}}
print c1['a1']
```

This will produce `{'e1': {}, 'e2': {}}`.
 
### lambda



### **opts

## Inheritance 
- [Python Inheritance](http://www.tutorialspoint.com/python/python_classes_objects.htm)
- [mininet Class diagram and doc](http://security.riit.tsinghua.edu.cn/~bhyang/mn_doc/mininet.topo.Topo-class.html) It provides quick [UML diagram]()


