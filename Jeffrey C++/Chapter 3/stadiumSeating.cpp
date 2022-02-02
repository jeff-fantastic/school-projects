#include <iostream>
#include <iomanip>
using namespace std;

#define CLASS_A_COST 15.00
#define CLASS_B_COST 12.00
#define CLASS_C_COST 9.00

int main(){
	//Define variables
	double classA, classB, classC;
	
	//Get info
	cout<<"How many seats have been bought for Class A, Class B, and Class C"<<endl;
	cin>>classA>>classB>>classC;
	
	//Calculate
	classA *= CLASS_A_COST;
	classB *= CLASS_B_COST;
	classC *= CLASS_C_COST;
	
	//Display info
	cout<<setprecision(2)<<showpoint<<fixed;
	cout<<"CLASS A COST  -  $"<<classA<<endl;
	cout<<"CLASS B COST  -  $"<<classB<<endl;
	cout<<"CLASS C COST  -  $"<<classC<<endl;
}
