#include <bits/stdc++.h>
using namespace std;

int n;
vector<int> l;
vector<int> dp;

// Recursive function with memoization
int solve_dp(int ind) {
    if (ind >= n) return 0;

    if (dp[ind] != -1) return dp[ind];

    int ans = (l[ind] == 1 ? 1 : 0);

    int first = solve_dp(ind + 2);
    int sec = solve_dp(ind + 3);

    int third = INT_MAX, fourth = INT_MAX;
    int ans2 = 0;

    if (ind + 1 < n) {
        if (l[ind + 1] == 1) {
            ans2 = ans + 1;
        } else {
            ans2 = ans;
        }

        third = solve_dp(ind + 3);
        fourth = solve_dp(ind + 4);
    }

    return dp[ind] = min({
        first + ans,
        sec + ans,
        third + ans2,
        fourth + ans2
    });
}

void solve() {
    cin >> n;
    l.resize(n);
    for (int i = 0; i < n; i++) cin >> l[i];

    dp.assign(n + 5, -1); // extra space for safety

    cout << solve_dp(0) << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}