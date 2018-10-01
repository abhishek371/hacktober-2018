import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int year = in.nextInt();
        if((year>=1700)&&(year<=1917))
        {
            if(year%4==0)
            {System.out.println("12.09."+year);}
            else
            {System.out.println("13.09."+year);}
        }
        if(year==1918)
        {System.out.println("26.09.1918");}
        if((year>1918)&&(year<=2700))
        {
            if(((year%4==0)&&(year%100!=0))||(year%400==0))
            {System.out.println("12.09."+year);}
            else
            {System.out.println("13.09."+year);}
        }
    }
}
