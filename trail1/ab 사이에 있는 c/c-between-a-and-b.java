import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int a, b, c;
        a = sc.nextInt();
        b = sc.nextInt();
        c = sc.nextInt();
        boolean k = false;
        for(int i = a; i <= b; i++){
            if(i % c == 0){
                k = true;
            }
        }
        if(k == true){
            System.out.println("YES");
        }
        else{
            System.out.println("NO");
        }
            

        }

    }
