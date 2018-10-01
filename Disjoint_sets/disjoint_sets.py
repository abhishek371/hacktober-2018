class Node:
	def __init__(self, rnk, d):
		self.rank = rnk
		self.parent = self
		self.data = d
		self.size=1


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
			self.members[v]=Node(0,v)


	def find_set(self,n):
		if n.parent != n:
			self.members[n.data].parent = self.find_set(n.parent)
		return n.parent
	
	def union(self, n1, n2):
		root_n1 = self.find_set(n1)
		root_n2 = self.find_set(n2)
		if root_n1.rank > root_n2.rank:
			self.members[root_n1.data].size += self.members[root_n2.data].size
			self.members[root_n2.data].parent = self.members[root_n1.data]
		elif root_n1.rank < root_n2.rank:
			self.members[root_n2.data].size += self.members[root_n1.data].size
			self.members[root_n1.data].parent = self.members[root_n2.data]
		else:
			self.members[root_n1.data].size += self.members[root_n2.data].size
			self.members[root_n2.data].parent = self.members[root_n1.data]
			self.members[root_n1.data].rank = root_n1.rank+1

def main():
	n=int(input("Enter no of Edges : "))
	print("Enter the edges(X to stop) :")
	S=Disjoint_sets()
	while True:
		t=input().split()
		if t[0]=='x':
			break
		v1=int(t[0])
		v2=int(t[1])
		S.make_set(v1)
		S.make_set(v2)
		S.union(S.get(v1),S.get(v2))
	d=dict()
	for m in S.members.values():
		print("Value : %s  Parent : %s  Size : %s" %(m.data,m.parent.data,m.parent.size))
		mem=m.parent.data
		if mem not in d:
			d[mem]=m.parent.size
	l=[]
	for i,k in d.items():
		l.append(k)
	print(l)


if __name__ == '__main__':
	main()