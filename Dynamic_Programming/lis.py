def lis(arr):
	memo={}
	for i in range(len(arr)):
		memo[i]=1
	for i in range(1,len(arr)):
		for j in range(0,i):
			if arr[i]>arr[j]:
				if memo[i]<memo[j]+1:
					memo[i]=memo[j]+1
	return max(memo)









def main():
	arr=[]
	print("Enter the numbers in the sequence(x to stop) :")
	while True:
		n=input()
		if n=='x':
			break
		arr.append(n)
	l=lis(arr)
	print("The length of the Longest Subsequence is :%s"%(l))


if __name__ == '__main__':
	main()