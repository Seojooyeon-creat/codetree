import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);

        int a, b, k;
        a = sc.nextInt();
        b = sc.nextInt();

        k = a > b ? a : b;

        System.out.println(k);
    }
}