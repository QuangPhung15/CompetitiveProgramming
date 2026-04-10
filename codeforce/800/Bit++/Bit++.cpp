#include <iostream>
using namespace std;

void solve() {
    int n, res = 0;
    cin >> n;

    for (int i = 0; i < n; i++) {
        string x;
        cin >> x;

        if (x[0] == '+' || x[2] == '+') {
            res++;
        } else {
            res--;
        }
    }

    cout << res << endl;
}

int main() {
    solve();
    return 0;
}