#include <iostream>
using namespace std;

void arrayLooping() {
    int numbers[5] = {1, 2, 3, 4, 5};
    for (int i = 0; i < 5; i++) {
        cout << numbers[i] << endl;
    }
}

int main() {
    arrayLooping();
    return 0;
}
