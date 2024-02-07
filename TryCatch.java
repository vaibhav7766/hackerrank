//https://www.hackerrank.com/challenges/java-int-to-string/problem?isFullScreen=true

import java.util.Scanner;

public class TryCatch {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.close();
        try{
            String s = Integer.toString(n);
            System.out.println("Good job");
        }
        catch(Exception e){
            System.out.println("Wrong answer");
        }
    }
}
