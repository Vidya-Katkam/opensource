import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int a[][] = new int[n][n];
        for(int i =0;i<n;i++) {
            for(int j=0;j<n;j++) {
                a[i][j]=s.nextInt();
            }
        }
        /*int res[][] = new int[n][n];
        for(int j =0;j<n;j++) {
            for(int i=0;i<n;i++) {
                res[j][i] = a[i][j];
            }
        }
        for(int i =0;i<n;i++) {
            for(int j=0;j<n;j++) {
                System.out.print(res[i][j]+" ");
            }
            System.out.println();
        }*/
        for(int i =0;i<n;i++) {
            for(int j=0;j<n;j++) {
                System.out.print(a[j][i]+" ");
            }
            System.out.println();
        }
    }
}
