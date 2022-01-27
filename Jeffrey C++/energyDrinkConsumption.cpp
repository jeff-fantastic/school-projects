#include <iostream>
using namespace std;

//This program will display the approximate number of customers that get a energy drink every week,
//and the approximate number of users who prefer citrus flavor.

int main(){
	//Declare Variables
	const double weeklyED  = 0.15,
				 citrusED  = 0.58,
				 userCount = 16500;
	int usersWeekly, usersCitrus;
	
	//Calculate
	usersWeekly = userCount * weeklyED;
	usersCitrus = usersWeekly * citrusED;
	
	//Display info
	cout<<"USERS SURVEYED    -  "<<userCount<<endl;
	cout<<"WEEKLY E.DRINKERS -  "<<usersWeekly<<endl;
	cout<<"CITRUS ENJOYERS   -  "<<usersCitrus;
}
