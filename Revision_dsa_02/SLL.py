class Node:
	def __init__(self, data):
		self.data = data
		self.ref = None
class LinkedList:
	def __init__(self):
		self.head = None

	def print_ll(self):
		if self.head is None:
			print("LL is empty")
		else:
			n = self.head
			while n is not None:
				print(n.data, "--->", end = " ")
				n = n.ref
	def add_begin(self, data):
		new_node = Node(data)
		new_node.ref = self.head
		self.head = new_node
	def add_end(self, data):
		new_node = Node(data)
		if self.head is None:
			new_node = self.head
		else:
			n = self.head
			while n.ref is not None:
				n = n.ref
			n.ref = new_node
	def add_after(self, data, x):
		n = self.head
		while n is not None:
			if n.data == x:
				break
			n = n.ref
		if n is None:
			print("Node is not present")
		else:
			new_node = Node(data)
			new_node.ref = n.ref
			n.ref = new_node
	def add_before(self, data, x):
		if self.head is None:
			print("LL is empty..")
			return
		if self.head.data == x:
			new_node = Node(data)
			new_node.ref = self.head
			self.head = new_node
			return
		n = self.head
		while n.ref is not None:
			if n.ref.data == x:
				break
			n = n.ref
		if n.ref is None:
			print("Node is not present")
		else:
			new_node = Node(data)
			new_node.ref = n.ref
			n.ref = new_node
	def insert_empty(self, data):
		if self.head is None:
			new_node = Node(data)
			self.head = new_node
		else:
			print("LL is not empty")
	def delete_begin(self):
		if self.head is None:
			print("LL is empty can't delete")
		else:
			self.head = self.head.ref
	def delete_end(self):
		if self.head is None:
			print("LL is empty can't delete")
		elif self.head.ref is None:
			self.head = None
		else:
			n = self.head
			while n.ref.ref is not None:
				n = n.ref
			n.ref = None
	def delete_by_value(self, x):
		if self.head is None:
			print("LL is empty")
			return
		if self.head.data == x:
			self.head = self.head.ref
		else:
			n = self.head
			while n.ref is not None:
				if n.ref.data == x:
					break
					n = n.ref
			if n.ref is None:
				print("Node is not present in the LL")
			else:
				n.ref = n.ref.ref

LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_end(12)
LL1.add_after(20, 10)
LL1.add_before(18, 12)
# LL1.insert_empty(15)
LL1.print_ll()
print()
LL1.delete_begin()
LL1.delete_end()
LL1.delete_by_value(20)
LL1.print_ll()