import java.util.Scanner;

public class qk {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String events = input.next();
        int count = 0;
        for(int i = 0 ; i < events.length()-1; i++) {
            for(int j = i+1 ; j < events.length() ; j++) {
                String itin = events.substring(i, j+1);
                String first = itin.substring(0,1);
                String last = itin.substring(itin.length()-1);
                if(!first.equals(last) && itin.lastIndexOf(first) == 0 && itin.indexOf(last) == itin.length()-1)
                    count++;
            }
        }
        System.out.println(count);
    }
}