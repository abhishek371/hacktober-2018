import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] s = new int[n];
        for(int i=0; i < n; i++){
            s[i] = in.nextInt();
        }
        int m=0,least=0,max,min,i;
        max=s[0];
        min=s[0];
        for(i=0;i<n;i++)
        {
            if(s[i]>max)
            {
                max=s[i];
                m=m+1;
            }
            if (s[i]<min)
            {
                min=s[i];
             least=least+1;
            }
        }
        System.out.print(m);
        System.out.print(" ");
          System.out.print(least);
}
}
