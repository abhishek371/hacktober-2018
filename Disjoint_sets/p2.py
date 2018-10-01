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
			#print("Found")
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
	
	def union(self, n1, n2,b):
		root_n1 = self.find_set(n1)
		root_n2 = self.find_set(n2)
		if root_n1==root_n2:
			#print("Both")
			return
		else:
			if root_n1.size+root_n2.size > b:
				return
			else:
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
	'''nmabfst = input().split()
	n = int(nmabfst[0])
	m = int(nmabfst[1])
	a = int(nmabfst[2])
	b = int(nmabfst[3])
	f = int(nmabfst[4])
	s = int(nmabfst[5])
	t = int(nmabfst[6])
	#membersInTheLargestGroups(n, m, a, b, f, s, t)'''
	m=int(input())
	S=Disjoint_sets()
	for i in range(m):
		v=input().split()
		v1=v[0]
		v2=v[1]
		#print(v1,v2)
		S.make_set(v1)
		S.make_set(v2)
		S.union(S.get(v1),S.get(v2),3)
	for m in S.members.values():
		print("Value : %s  Parent : %s  Size : %s" %(m.data,m.parent.data,m.parent.size))
		
if __name__ == '__main__':
	main()