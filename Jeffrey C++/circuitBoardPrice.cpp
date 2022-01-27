#include <iostream>
using namespace std;

//This program will calculate the selling price of a circuit board that costs 14.95.
//The company only makes a sale profit of 35%.

#define SALE_PROFIT_PERCENT 0.35

int main(){
	//Declare Varaibles
	const double circPrice = 14.95;
	double salePrice;
	
	//Calculate
	salePrice = circPrice * SALE_PROFIT_PERCENT;
	
	//Display information
	cout<<"Circuit Board Price  -  "<<circPrice<<endl;
	cout<<"Sale Price           -  "<<salePrice<<endl;
}
