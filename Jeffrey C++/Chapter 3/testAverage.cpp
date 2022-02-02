#include <iostream>
#include <iomanip>
using namespace std;


int main(){
	//Declare variables
	double scores[] = {
		0.0,
		0.0,
		0.0,
		0.0,
		0.0,
	};
	double accumulator = 0.0;
	
	//Get info
	cout<<"Please enter your five test scores."<<endl;
	cin>>scores[0]>>scores[1]>>scores[2]>>scores[3]>>scores[4];
	
	//Calculate
	for (int i = 0; i < 5; i++){
		accumulator += scores[i];
	}
	accumulator /= 5;
	
	//Display info
	cout<<setprecision(1)<<fixed;
	for (int i = 0; i < 5; i++){
		cout<<"SCORE "<<i<<"  -  "<<scores[i]<<endl;
	}
	cout<<"-----------------------"<<endl;
	cout<<"SCORE AVERAGE  -  "<<accumulator;
}
