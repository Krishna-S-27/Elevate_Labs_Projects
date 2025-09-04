#include <iostream>  
using namespace std;   // Bad practice: using-directive  

// Function with some complexity
int badFunction(int a, int b) {  
    int result = 0;  

    if (a > 0) {
        if (b > 0) {
            for (int i = 0; i < a; i++) {
                if (i % 2 == 0) {
                    result += b;
                } else {
                    result -= b;
                }
            }
        } else {
            result = -1;
        }
    } else {
        result = -2;
    }

    return result;
}

int main() {  
    int x = 5;
    int y = 10;
    cout << badFunction(x, y) << endl;
    return 0;
}
