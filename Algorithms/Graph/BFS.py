#Breadth First Search

class Adjacent_list:
	def __init__(self,n):
		self.lis=[[] for _ in range(n)]

class Queue:
	def __init__(self):
		self.queue=[]

	def enqueue(self,v):
		self.queue.append(v)

	def dequeue(self):
		x = self.queue.pop(0)
		return x

	def is_Empty(self):
		return len(self.queue) == 0



class BFS(Adjacent_list):
	
	def add_edges(self,v1,v2):
		self.lis[v1].append(v2)
		self.lis[v2].append(v1)

	def bfs(self,source):
		visited=[]
		Q=Queue()
		Q.enqueue(source)
		visited.append(source)
		print(source,end=" ")
		while not Q.is_Empty():
			node=Q.dequeue()
			for neighbour in self.lis[node]:
				if neighbour not in visited:
					visited.append(neighbour)
					print(neighbour,end=" ")
					Q.enqueue(neighbour)


def main():
	
	n=int(input("Enter the number of vertices:"))
	B=BFS(n)
	#creating an object for both the classes

	print ("Enter the edges(x to stop):")
	while True:
		e=input().split()
		if e[0]=='x':
			break
		else:
			v1,v2=map(int,e)
			B.add_edges(v1,v2)

	print (B.lis)
			
	print("Enter the source vertex:")
	source=int(input())
	B.bfs(source)

if __name__ == '__main__':
	main()
