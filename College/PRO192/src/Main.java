import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("n = ");
        long n = input.nextLong();

        if (isPrime(n))
            System.out.println(n + " is a prime.");
        else
            System.out.println(n + " is not a prime.");
    }

    public static boolean isPrime(long n) {
        if (n <= 3)
            return n > 1;
        if (n % 2 == 0 || n % 3 == 0)
            return false;
        for (int i = 2; i <= Math.sqrt(n); i += 6)
            if (n % i == 0 || n % (i + 2) == 0)
                return false;
        return true;
    }
}