import java.util.Scanner;

public class qm {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int numProb = input.nextInt();
        for(int i = 0 ; i < numProb ; i++) {
            double w = input.nextDouble();
            double g = input.nextDouble();
            double h = input.nextDouble();
            double r = input.nextDouble();
            double w1 = w / ( (h-r)/(g-r) + 1);
            double w2 = w - w1;
            double wBig = w1 > w2 ? w1 : w2;
            double wSmall = w1 < w2 ? w1 : w2;
            double hBig = h > g ? h : g;
            double hSmall = h < g ? h : g;
            double minLength = Math.sqrt(w*w + (g-h)*(g-h));
            double maxLength;
            if(r < hSmall)
                maxLength = Math.sqrt(wBig*wBig + (hBig-r) * (hBig-r)) + Math.sqrt(wSmall*wSmall + (hSmall-r)*(hSmall-r));
            else
                maxLength = minLength;
            System.out.println(minLength + " " + maxLength); 
        }
    }

}