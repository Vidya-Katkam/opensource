import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        for(int i=1;i<=n;i++) {
            for (int j=1;j<=i;j++) {
                System.out.print(j);
            }
            for (int j=1;j<=(n-i)*2;j++) {
                System.out.print(" ");
            }
            for (int j=i;j>=1;j--) {
                System.out.print(j);
            }
            System.out.println();
        }
    }
}
