#include <iostream>
#include <math.h>

using namespace std;

//previous version
//int divisor_number(int x){
//	if(x == 0)
//		return 0;
//
//	int divisor_number = 0;
//	for (int i = 1; i <= x; i++)
//		if(x%i == 0)
//			divisor_number++;
//	return divisor_number;
//}

int divisor_number(int x){
	if(x == 0)
		return 0;

	int divisor_number = 0;
	for (int i = 1; i <= round(sqrt(x)); i++)
		if(x%i == 0)
			divisor_number+=2;
	return divisor_number;
}

int main(){
	int triangle_number = 1;
	int triangle_value = 1;
	int threshold_divisors = 500;

	while(true){	
		if(divisor_number(triangle_value) > threshold_divisors){
			cout << "The #" << triangle_number << ": " << triangle_value << " has over " << threshold_divisors << " divisors." << endl;
			break;
		} else {
			triangle_number++;
			triangle_value += triangle_number;
		}
	}

	return 0;
}
