a = [1,2,3,4,'hi','raghu']
c = [9,8,6,5,4,3,2,'left']
# print('the length of list a is:', len(a),'and list is: ',a)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# making list using "list() Method" 
# b = list(('raghu','bhavy',1,2))
# print(type(b),b)

# print(a[1],a[-1],a[2:],a[-4:-1])

# To insert a list item at a specified index, use the "insert()" method. The insert() method inserts an item at the specified index:
# a.insert(2,'hello')
# print(a)

# To add an item to the end of the list, use the "append()" method
# a.append("RKU")
# print(a)

# To append elements from another list to the current list, use the extend() method.
# a.extend(c)
# print(a)
# OP -> [1, 2, 3, 4, 'hi', 'raghu', 9, 8, 6, 5, 4, 3, 2, 'left']

# The remove() method removes the specified item.
# a.remove('hi')
# print(a)
# If there are more than one item with the specified value, the remove() method removes the first occurrence:
# thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
# thislist.remove("banana")
# print(thislist)

# The pop() method removes the specified index.
# a.pop(0)
# print(a)
# OP -> [2, 3, 4, 'hi', 'raghu']
# If you do not specify the index, the pop() method removes the last item.

# The "del" keyword also removes the specified index:
# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)
# The del keyword can also delete the list completely.
# thislist = ["apple", "banana", "cherry"]
# del thislist

# The "clear()" method empties the list. The list still remains, but it has no content.
# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)