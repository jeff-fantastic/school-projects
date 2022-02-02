#include <iostream>
#include <iomanip>
using namespace std;

int main(){
	//Declare variables
	string month1, month2, month3;
	double rFall1, rFall2, rFall3, rAvg;
	
	//Get info
	cout<<"Please enter three months."<<endl;
	cin>>month1>>month2>>month3;
	cout<<"What is the rainfall for "<<month1<<", "<<month2<<", "<<month3<<"?"<<endl;
	cin>>rFall1>>rFall2>>rFall3;
	
	//Calculate
	rAvg = (rFall1 + rFall2 + rFall3) / 3;
	
	//Display info
	cout<<"The average rainfall for "<<month1<<", "<<month2<<" and "<<month3<<" is "<<rAvg<<" inches.";
}
