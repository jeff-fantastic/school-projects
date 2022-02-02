#include <iostream>
#include <iomanip>
using namespace std;

#define ADULT_TICKET_PRICE 10.00
#define CHILD_TICKET_PRICE 6.00
#define THEATER_PROFIT_PERCENT 0.20

int main(){
	//Define variables
	int adultSales, childSales;
	double grossProfit, netProfit, distProfit;
	string movieName;
	
	//Get input
	cout<<"What is the name of the movie?"<<endl;
	getline(cin, movieName);
	cout<<"How many tickets were sold to Adults?"<<endl;
	cin>>adultSales;
	cout<<"How many tickets were sold to Children?"<<endl;
	cin>>childSales;
	
	//Calculate
	grossProfit = (adultSales * ADULT_TICKET_PRICE) + (childSales * CHILD_TICKET_PRICE);
	netProfit = grossProfit * THEATER_PROFIT_PERCENT;
	distProfit = grossProfit - netProfit;
	
	//Display information
	cout<<fixed<<endl;
	cout<<"Movie Title                       \""<<movieName<<"\""<<endl;
	cout<<"Adult Tickets Sold                "<<adultSales<<endl;
	cout<<"Child Tickets Sold                "<<childSales<<endl;
	cout<<"Gross Box Office Profit           $"<<setprecision(2)<<grossProfit<<endl;
	cout<<"Net Box Office Profit             $"<<setprecision(2)<<netProfit<<endl;
	cout<<"Amount Paid to Distributor        $"<<setprecision(2)<<distProfit<<endl;
}
