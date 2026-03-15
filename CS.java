//JAVA0016_某天是一年中第几天
/**
输入某年某月某日，判断这一天是这一年的第几天？
程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于3时需考虑多加一天。
例如：
输入：2020<回车>  1<回车>  1<回车>
返回：这天是2020年的第1天
 **/
import java.util.Scanner;
//import java.util.Random;
//import java.io.*;
public class CS {
	public static void main(String[] args) throws InterruptedException {
    try {
   	//System.out.println("Please Input ： ");
	//Scanner csscan = new Scanner(System.in).useDelimiter("\\D");//匹配非数字
	System.out.print("请输入当前日期（年 月 日）:");
    Scanner csscan = new Scanner(System.in);
	int int_Year = csscan.nextInt();
	int int_Month = csscan.nextInt();
	int int_Date = csscan.nextInt();
	csscan.close();
	System.out.println("这天是"+int_Year+"年的第"+DayinYear(int_Year,int_Month,int_Date)+"天");
  	}catch (Exception e) {
    	   System.out.println(" -- 计算错误 --");
        }
    	finally{
    	   System.out.println(" -- 完毕 --");
        }
     }//  public static void main(String[] args) {
	private static int DayinYear(int fc_year, int fc_month, int fc_date){
		int n = 0;
		int[] month_date = new int[] {0,31,28,31,30,31,30,31,31,30,31,30};
		if((fc_year%400)==0 || ((fc_year%4)==0)&&((fc_year%100)!=0))
		  month_date[2] = 29;
		for(int i=0;i<fc_month;i++)
		  n += month_date[i];
		return n+fc_date;
	}
}//public class cs {
