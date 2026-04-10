#include <iostream>
using namespace std;

void solve() {
    int n;
    cin >> n;
    
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;

        if (s.size() <= 10) {
            cout << s << endl;
        } else {
            cout << s[0] << to_string(s.size() - 2) << s[s.size() - 1] << endl;
        }
    }
}

int main() {
    solve();
    return 0;
}