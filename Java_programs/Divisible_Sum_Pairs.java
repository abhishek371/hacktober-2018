import java.util.Scanner;
class divisible_sum
{
	public static void main(String args[])
	{
		int n,k,j,i,count=0;
		Scanner in=new Scanner(System.in);
		n=in.nextInt();
		k=in.nextInt();
		int[] a=new int[n];
		for(i=0;i<n;i++)
		{
			a[i]=in.nextInt();
		}
		for(i=0;i<n;i++)
		{
			for(j=i+1;j<n;j++)
			{
				if(((a[i]+a[j])%k)==0)
				{
					count=count+1;
				}
			}
		}
		System.out.println(count);

	}
}
