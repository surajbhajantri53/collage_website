import java.util.Scanner;

public class Student {
    String studentName;
    int studentAge;
    int sub1;
    int sub2;
    

    Student(String studentName,int studentAge,int sub1,int sub2){
        this.studentName=studentName;
        this.studentAge=studentAge;
        this.sub1=sub1;
        this.sub2=sub2;
        
    }
    int Total(int sub1,int sub2){
        return sub1+sub2;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter student Name: ");
        String studentName=scanner.next();
        System.out.println("Enter student age: ");
        int studentAge=scanner.nextInt();
        System.out.println("Enter subject 1 Marks : ");
        int sub1=scanner.nextInt();
        System.out.println("Enter Subject 2 marks : ");
        int sub2=scanner.nextInt();

       Student student = new Student(studentName, studentAge, sub1, sub2);
       int total= student.Total(sub1, sub2);
       System.out.println("Name : "+student.studentName);
       System.out.println("Age : "+student.studentAge);
       System.out.println("Subject 1 marks : "+student.sub1);
       System.out.println("Subject 2 Marks : "+student.sub2);
        System.out.println("The Total Marks is : "+total+"\n The average is "+total/2 );

        scanner.close();
        
    }
}
