import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int s = in.nextInt();
        int n = in.nextInt();
        int m = in.nextInt();
        int[] k = new int[n];
        int i,j,sum,max=-1;
        for(i=0;i < n;i++){
            k[i] = in.nextInt();
        }
        int[] d = new int[m];
        for( i=0; i < m;i++){
            d[i] = in.nextInt();
        }
        //  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
        for(i=0;i < n;i++){
            for(j=0;j<m;j++)
            {
                sum=k[i]+d[j];
                if((sum>max)&&(sum<=s))
                {
                    max=sum;
                }
                    
            }
        }
       
        System.out.println(max);
        
       
    }
}
