import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int[] h = new int[26];
        for(int i=0; i < 26; i++){
            h[i] = in.nextInt();
        }
        String word = in.next();
        int l=word.length();
        char ch;
        int height;
        int max=0;
        //System.out.println(l);
        for(int i=0;i<l;i++)
        {
            ch=word.charAt(i);
            int a=(int)ch-96;
            //System.out.println(a);
            a=a-1;
            height=h[a];
            if(max<height)
            {
                max=height;
            }
        }
        System.out.println(l*max);
    }
}
