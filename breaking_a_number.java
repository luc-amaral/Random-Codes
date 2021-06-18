//Breaking a number (decimal)

import java.lang.Math;
import java.util.Scanner;

public class Main
{
	public static void main(String[] args) {
		//System.out.println("Hello World");
		Scanner input = new Scanner(System.in);
	    	double number = input.nextDouble();
		System.out.println(Math.floor(number));
	}
}
