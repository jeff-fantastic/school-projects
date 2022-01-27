#include <iostream>
using namespace std;

//Find the average of the values 28, 32, 37, 24, and 33

int main(){
	//Declare Variables
	const double v1 = 28,
				 v2 = 32,
				 v3 = 37,
				 v4 = 24,
				 v5 = 33;
	double avg;
	
	//Calculate
	avg = (v1+v2+v3+v4+v5)/5;
	
	//Display info
	cout<<"The average is "<<avg;
}
