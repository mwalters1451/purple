
#include <iostream>
#include <string>
using namespace std;

double calculateCharges(double hours)
{
	double charge = 2;

	if(hours > 3)
    {
        double time_spent = hours - 3;

        charge += time_spent * 0.5;

    }


	if(charge > 10.0)
    {
        charge = 10.0;
    }

	return charge;

}


int main()
{
	double car1 = 0;
	double car2 = 0;
	double car3 = 0;

	cout << "numbers of hours parked (car1): " << endl;
	cin >> car1;
	cout << "numbers of hours parked (car2): " << endl;
	cin >> car2;
	cout << "numbers of hours parked (car3): " << endl;
	cin >> car3;

	double total_hours = car1 + car2 + car3;

	double total_charges = calculateCharges(car1)+ calculateCharges(car2) + calculateCharges(car3);

	cout << "Car     " << "Hours     " << "Charges" <<endl;
	cout << "1" << "      " << car1 << "       " << calculateCharges(car1) << endl;

    cout << "2" << "      " << car2 << "       " << calculateCharges(car2) << endl;
    cout << "3" << "      " << car3 << "       " << calculateCharges(car3) << endl;
    cout << "TOTAL    " << total_hours  << "     "<< total_charges;
}
