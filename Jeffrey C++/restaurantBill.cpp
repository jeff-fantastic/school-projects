#include <iostream>
using namespace std;

#define TAX 0.0675
#define TIP 0.20

// This program will compte the tax and tip for a resturaunt bill.
// The tip will be 20% of the total after adding tax. Display the meal cost,
// tax amount, tip amount, and total bill.

int main(){
	//Declare variables
	const double price = 88.67;
	double priceTax, priceTip, priceTotal;
	
	//Calculate
	priceTax = price * TAX;
	priceTip = (price + priceTax) * TIP;
	priceTotal = price + priceTax + priceTip;
	
	//Display information
	cout<<"Initial Price  -  "<<price<<endl;
	cout<<"Price Tax      -  "<<priceTax<<endl;
	cout<<"Tip            -  "<<priceTip<<endl;
	cout<<"--------------------------------"<<endl;
	cout<<"Total Price    -  "<<priceTotal;
}
