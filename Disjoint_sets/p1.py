#!/bin/python3

import os
import sys

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
		if root_n1==root_n2:
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
	#n=int(input("Enter no of Edges : "))
	#x=int(input())
	#print("Enter the edges(X to stop) :")
	'''S=Disjoint_sets()
	while True:
		t=input().split()
		if t[0]=='x':
			break
		v1=int(t[0])
		v2=int(t[1])
		S.make_set(v1)
		S.make_set(v2)
		S.union(S.get(v1),S.get(v2))'''
	nq=input().split()
	n=int(nq[0])
	q=int(nq[1])
	s=Disjoint_sets()
	for i in range(1,n+1):
		s.make_set(i)
	for i in range(q):
		a=input().split()
		if a[0]=="1":
			a1=int(a[1])
			a2=int(a[2])
			s.union(s.get(a1),s.get(a2))
		if a[0]=="2":
			c=int(a[1])
			d=dict()
			for m in s.members.values():
				#print("Value : %s  Parent : %s  Size : %s" %(m.data,m.parent.data,m.parent.size))
				mem=m.parent.data
				if mem not in d:
					d[mem]=m.parent.size
			l=[]
			for i,k in d.items():
				l.append(k)
			#print(l)
			l.sort()
			'''res = 0
			for i in range(len(l)): 
				j = i+1
				while (j < len(l) and l[j] - l[i] >= c):
					res += 1
					j += 1
			print(res)'''
			low = 0
			high = n-1
			result = 0
			while (low < high):
     
        # If current left and current
        # right have sum smaller than x,
        # the all elements from l+1 to r
        # form a pair with current l.
				if (l[low] - l[high] > c):
					result += (high - l)
					low =low+ 1
         
 
        # Move to smaller value
				else:
					high =high- 1
 
			return result
 



if __name__ == '__main__':
	main()