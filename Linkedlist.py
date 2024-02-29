
class Node:
    def __init__(self,value):	
        self.value = value
        self.next = None
    
class Linkedlist:
	def __init__(self):
    
		self.head = None
		self.tail = None
		self.current = None
		self.previous = None

	def insertNode(self,value):
    
		newNode = Node(value)
        
		if self.head == None:
			self.head = newNode
			self.tail = newNode
            
		else:
			self.tail.next = newNode        
			self.tail = newNode
            
	def search(self,value):
    
		self.current = self.head
		bol = False
		while (self.current != None and bol == False):
        
			if self.current.value == value:
				print("Value was found")
				bol = True
                
			self.current = self.current.next
		
		if bol == False:
        
			print("Value was not found")

	def delate(self,value):
    
		self.current = self.head
        
		self.previous = self.head
		
		if self.head.value == value:
        
			self.head = self.head.next
			
			del(self.current)
            
		if self.tail.value == value:

			while(self.current != self.tail):

				self.previous = self.current
				self.current = self.current.next

			self.tail = self.previous
			del(self.current)
            
		if self.tail.value != value and self.head.value != value:

			while(self.current.value != value):

				self.previous = self.current
				self.current = self.current.next
			
			self.previous.next = self.current.next
			del(self.current)
	
	def printList(self):

		self.current = self.head
		while self.current != None:

			print(self.current.value)

			self.current = self.current.next
