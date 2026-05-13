#include <iostream>

using namespace std;

int main() {
    // 변수 선언
    int a = 1;
    int b = 5;
    int c = 3;
    
    // 값 변경
    a = c;
    a = a + c;
    b = b - c;
    
    // 출력
    cout << a;
    cout << "\n";
    cout << b;
    cout << "\n";
    cout << c;
    return 0;
}
