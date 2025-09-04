// Poor style: long method, deeply nested ifs, unused imports
import java.util.List;

public class BadClass {
    public static void main(String[] args) {
        int a = 5;
        int b = 10;
        if (a > 0) {
            if (b > 0) {
                if (a > b) {
                    System.out.println("a bigger");
                } else if (a == b) {
                    System.out.println("equal");
                } else {
                    System.out.println("b bigger");
                }
            } else {
                System.out.println("b not positive");
            }
        } else {
            System.out.println("a not positive");
        }
    }

    public void unusedMethod() {
        // never called
    }
}
