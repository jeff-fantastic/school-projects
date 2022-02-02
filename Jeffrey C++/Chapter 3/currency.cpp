#include <iostream>
#include <iomanip>
using namespace std;

#define YEN_PER_DOLLAR 98.93
#define EUROS_PER_DOLLAR 0.74

int main(){
	//Define variables
	double dollarAmount, yenConv, euroConv;
	
	//Get input
	cout<<"How many US dollars would you like to convert?"<<endl;
	cin>>dollarAmount;
	
	//Calculate
	yenConv = dollarAmount * YEN_PER_DOLLAR;
	euroConv = dollarAmount * EUROS_PER_DOLLAR;
	
	//Display info
	cout<<fixed<<setprecision(2)<<showpoint;
	cout<<"US DOLLAR           $"<<dollarAmount<<endl;
	cout<<"YEN                 ¥"<<yenConv<<endl;
	cout<<"EURO                €"<<euroConv<<endl;
}
