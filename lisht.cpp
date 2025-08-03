#include <iostream>
#include <cmath>
using namespace std;

// Function that multiplies x by tanh(x)
float Lisht(float x) {
    return x * tanh(x);
}

int main() {
    float result = Lisht(5.5f); // Call Lisht with 5.5
    cout << "Result: " << result << endl; // Output the result
    return 0;
}
