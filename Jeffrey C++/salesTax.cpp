#include <iostream>
using namespace std;

//This is a program for sales tax. It will compute the total sales tax on a 95$ purchase.
//This is assuming that the sales tax is 4%, and the county's is 2%.

#define SALES_TAX 0.04
#define COUNTY_TAX 0.02

int main(){
	//Declare variables
	const double sale = 95.00;
	double saleTax, saleCountyTax, saleTotal;
	
	//Calculate
	saleTax = sale * SALES_TAX;
	saleCountyTax = sale * COUNTY_TAX;
	saleTotal = sale + saleTax + saleCountyTax;
	
	//Display information
	cout<<"Original Sale Price  -  "<<sale<<endl;
	cout<<"Sales Tax  -  "<<saleTax<<endl;
	cout<<"County Tax  -  "<<saleCountyTax<<endl;
	cout<<"Total Sale Price  -  "<<saleTotal<<endl;
}
