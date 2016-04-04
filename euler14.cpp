#include <iostream>

using namespace std;

//return the collatz value for the value until it reaches 1
//chainsize is a reference to the variable counting how big the chain is
//chainsize must start at 1
//verbose states whether the function gives output or not through the calculation of the collatz chain
int collatz(int x, int & chainsize, bool verbose = false){
	if(verbose) {
		if(x == 1)
			cout << x << endl;
		else
			cout << x << " -> ";
	}

	if(x == 1 || x == 0) {
		return x;
	} else {
		if(x%2==0) {
			chainsize++;
			return collatz(x/2, chainsize, verbose);
		} else {
			chainsize++;
			return collatz(3*x + 1, chainsize, verbose);
		}
	}
}

//iteractive implementation of collatz
int iteractive_collatz(long x){
	//chainsize starts at 1
	int chainsize = 1;

	//while x > 1
	for (int i = 0; x > 1; i++){
		//if x is odd
		if(x%2){
			x*=3; ++x;
			chainsize++;
		} else {
		//if x is even
			x/=2;
			chainsize++;
		}
	}
	return chainsize;
}

int main(){
//	int chainsize = 1;
//	collatz(113383, chainsize);
//	cout << chainsize << endl;

//	cout << iteractive_collatz(837799) << endl;

	int maxchainsize=1, maxcollatznumber=1;
	int maxnumber = 1000000;
//
//	int chainsize = 1;
//
//	for(int i = 0; i < maxnumber; i++){
//		cout << i << endl;
//		chainsize = 1;
//		collatz(i, chainsize);
//
//		if(chainsize > maxchainsize){
//			maxchainsize = chainsize;
//			maxcollatznumber = i;
//		}
//	}
//
//	cout << "The biggest collatz sequence under " << maxnumber << " is " << maxchainsize << " long, starting at " << maxcollatznumber << endl;

	for(int i = 0; i < maxnumber; i++){
		int chainsize = iteractive_collatz(i);
		if (chainsize > maxchainsize){
			maxchainsize = chainsize;
			maxcollatznumber = i;
		}
	}

	cout << "The biggest collatz sequence under " << maxnumber << " is " << maxchainsize << " long, starting at " << maxcollatznumber << endl;

	return 0;
}
