#include <iostream>

int main(void) {
    int a, b, c, d, temp;
    std::cout << "a = "; std::cin >> a;
    std::cout << "b = "; std::cin >> b;
    std::cout << "c = "; std::cin >> c;
    std::cout << "d = "; std::cin >> d;

    if (c < d) {
        temp = d;
        d = c;
        c = temp;
    }
    if (b < c) {
        temp = c;
        c = b;
        b = temp;
    }
    if (a < b) {
        temp = b;
        b = a;
        a = temp;
    }
    if (c < d) {
        temp = d;
        d = c;
        c = temp;
    }
    if (b < c) {
        temp = c;
        c = b;
        b = temp;
    }
    if (a < b) {
        temp = b;
        b = a;
        a = temp;
    }

    std::cout << "max = " << a << std::endl;
    std::cout << "min = " << d << std::endl;

    return 0;
}