class Node:
	def __init__(self, rnk, d):
		self.rank = rnk
		self.parent = self
		self.data = d
		self.adj_list=[]


class Adjacent_list:
	def __init__(self,n):
		self.lis=[[] for _ in range(n)]

	def add_edges(self,v1,v2):
		self.lis[v1].append(v2)
		self.lis[v2].append(v1)


class Disjoint_sets:
	def __init__(self):
		self.members=dict()

	def get(self,v):
		if v in self.members:
			return self.members[v]
		else:
			return None

	def make_set(self,v):
		if v not in self.members:
			N=Node(0,v)
			self.members[v]=N




	def find_set(self,n):
		if n.parent != n:
			self.members[n.data].parent = self.find_set(n.parent)
		return n.parent
	
	def union(self, n1, n2):
		root_n1 = self.find_set(n1)
		root_n2 = self.find_set(n2)
		if root_n1.rank > root_n2.rank:
			self.members[root_n2.data].parent = self.members[root_n1.data]
		elif root_n1.rank < root_n2.rank:
			self.members[root_n1.data].parent = self.members[root_n2.data]
		else:
			self.members[root_n2.data].parent = self.members[root_n1.data]
			self.members[root_n1.data].rank = root_n1.rank+1


	def isCycle(self,A):
		for i in self.members.values():
			#print(i)
			for j in A.lis[i.data]:
				if i.parent.data==self.members[j].parent:
					return True



def main():
	n=int(input("Enter no of Edges : "))
	print("Enter the edges(X to stop) :")
	A=Adjacent_list(n)
	S=Disjoint_sets()
	while True:
		t=input().split()
		if t[0]=='x':
			break
		v1=int(t[0])
		v2=int(t[1])
		A.add_edges(v1,v2)
		S.make_set(v1)
		S.make_set(v2)
		S.union(S.get(v1),S.get(v2))

	for m in S.members.values():
		print("Value : %s Parent : %s" %(m.data,m.parent.data))

	c=S.isCycle(A)
	if c==True:
		print("Cycle Found")
	else:
		print("No cycle present")

if __name__ == '__main__':
	main()