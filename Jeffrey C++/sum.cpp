#include <iostream>
using namespace std;

int main(){
	//declare variables
	double num1 = 0;
	double num2 = 0;
	double sum = 0;
	
	//user input
	cout<<"We will add two numbers."<<endl;
	cout<<"Enter the first number. ";
	cin>>num1;
	cout<<"Enter the second number. ";
	cin>>num2;
	
	//calculate
	sum = num1 + num2;
	
	//display answer
	cout<<"The sum of "<<num1<<" and "<<num2<<" is "<<sum;
	
	return 0;
}
