#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main(){
//	Generating random Numbers
	srand(time(0));
	int age = rand() % 100;
	cout << age;
    return 0;
}
