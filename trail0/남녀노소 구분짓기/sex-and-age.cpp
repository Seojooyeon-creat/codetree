#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n;
    int m;
    cin >> n;
    cin >> m;
    if(n == 0){
        if(m >= 19) cout << "MAN";
        else cout << "BOY";
    }
    else{
        if(m >= 19) cout << "WOMAN";
        else cout << "GIRL";
    }

    return 0;
}