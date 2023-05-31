#include <iostream>

using namespace std;

int main() {
    int i = 0;
    do {
        if (i == 2) {
            continue;;
        }
        cout << i << endl;
        i++;
    }
    while(i < 5);

    return 0;
}