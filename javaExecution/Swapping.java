import java.util.Scanner;

public class Swapping {
    public static void main(String[] args) {
        
        Scanner scanner= new Scanner(System.in);
        System.out.println("Enter value! for Swapping 2 Numbers :\n");
        int a=scanner.nextInt();
        System.out.println("Enter second number for swapping two Numbers: \n");
        int b=scanner.nextInt();
        System.out.println("Before swapping values are a= "+a+" and b= "+b);
        a=a^b;
        b=a^b;
        a=a^b;
        System.out.println("After Swapping the values are a= "+a+" and b= "+b);


        scanner.close();
    }
}
