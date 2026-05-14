#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a, b, i;
    cin >> a >> b;
    for(i=b; i > a - 1; i-=1){
        cout << i << " ";
    }
    return 0;
}