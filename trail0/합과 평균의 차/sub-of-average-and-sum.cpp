#include <iostream>

using namespace std;

int main() {
    // 변수 선언
    int a, b, c;

    // 입력
    cin >> a >> b >> c;
    
    // 출력
    cout << a + b + c << endl;
    cout << (a + b + c) / 3 << endl;
    cout << (a + b + c) - (a + b + c) / 3 << endl;
    return 0;
}

