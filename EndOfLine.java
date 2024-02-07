//https://www.hackerrank.com/challenges/java-end-of-file/problem?isFullScreen=true

import java.util.Scanner;

public class EndOfLine {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        for(int i = 1; scan.hasNext(); i++){
            String x = scan.nextLine();
            System.out.println(i+" "+x);
        }
        scan.close();
    }
}
