import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int n;
        n = sc.nextInt();
        boolean k = false;

        for(int i = 2; i <= n - 1; i++){
            if(n % i == 0){
                k = true;
            }
        }

        if(k == true){
            System.out.println("C");
        }
        else{
            System.out.println("N");
        }
    }
}