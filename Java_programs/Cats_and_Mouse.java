import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int q = in.nextInt();
        for(int a0 = 0; a0 < q; a0++){
            int x = in.nextInt();
            int y = in.nextInt();
            int z = in.nextInt();
            int a=z-x;
            if (a<0)
                    a=-a;
            int b=z-y;
            if (b<0)
                    b=-b;
            if (a>b)
            {
                System.out.println("Cat B");
            }
            else if (a<b)
            {
                System.out.println("Cat A");
            }
            else
            {
                System.out.println("Mouse C");
            }
        }
    }
}
