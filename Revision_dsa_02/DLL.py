class Node:
	def __init__(self, data):
		self.data = data
		self.nref = None
		self.pref = None
class doublyLL:
	def __init__ (self):
		self.head = None
	def print_ll(self):
		if self.head is None:
			print("LL is empty.")
		else:
			n = self.head
			while n is not None:
				print(n.data, "--->", end = " ")
				n = n.nref
	def print_ll_reverse(self):
		if self.head is None:
			print("LL is empty")
		else:
			n = self.head
			while n.nref is not None:
				n = n.nref
			while n is not None:
				print(n.data, "--->", end = " ")
				n = n.pref
	def insert_empty(self, data):
		if self.head is None:
			new_node = Node(data)
			self.head = new_node
		else:
			print("LL is not empty")
	def add_begin(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
		else:
			new_node.nref = self.head
			self.head.pref = new_node
			self.head = new_node

dll = doublyLL()
dll.insert_empty(10)
dll.add_begin(20)
dll.print_ll()