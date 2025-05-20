#include <iostream>
#include <vector>
using namespace std;

void solve() {
    int n, k, res = 0;
    vector<int> scores;
    cin >> n >> k;

    for (int i = 0; i < n; i++) {
        int a;
        cin >> a;
        scores.push_back(a);
    }

    for (int c : scores) {
        if (c > 0 && c >= scores[k - 1]) {
            res++;
        }
    }

    cout << res << endl;
}

int main() {
    solve();
    return 0;
}