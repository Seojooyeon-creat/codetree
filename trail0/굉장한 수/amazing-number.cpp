#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n;
    cin >> n;
    if(n % 2 == 0 and n % 5 == 0) cout << "true";
    else if(n % 2 == 1 and n % 3 == 0) cout << "true";
    else cout << "false";
    return 0;
}