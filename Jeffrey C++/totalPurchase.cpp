#include <iostream>
using namespace std;

//A customer in a store is purchasing 5 items. Apply sales tax and show each item's price,
//the subtotal, the amount of sales tax, and the final total.

#define SALES_TAX 0.07

int main(){
	//Declare variables
	const double item[] = {
		15.95,
		24.95,
		6.95,
		12.95,
		3.95,
	};
	double subTotal, taxTotal, finalTotal;
	
	//Calculate
	subTotal = item[0]+item[1]+item[2]+item[3]+item[4];
	taxTotal = subTotal * SALES_TAX;
	finalTotal = subTotal + taxTotal;
	
	//Display info
	for (int i = 0; i < 5; i++){
		cout<<"ITEM "<<i<<"       -  "<<item[i]<<endl;
	}
	cout<<"SUBTOTAL     -  "<<subTotal<<endl;
	cout<<"TAX TOTAL    -  "<<taxTotal<<endl;
	cout<<"--------------------------------"<<endl;
	cout<<"FINAL TOTAL  -  "<<finalTotal<<endl;
}
