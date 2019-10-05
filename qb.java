import java.util.Scanner;
public class qb {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		double l1 = input.nextDouble();
		double l2 = input.nextDouble();
		double M = l1 < l2 ? l1 : l2;
		double N = l1 > l2 ? l1 : l2;
		long count = 0;
		for(double i = 0.5 ; i < M ; i+=1) {
			double y = N / M * i;
			if(y%1 == 0.5)
				count++;
		} 
		System.out.println(count);
	}

}
