#include <bits/stdc++.h>
using namespace std;

int getInt() {
    int x;
    cin >> x;
    return x;
}

vector<long long> getIntList() {
    int n;
    return {};
}

void solve() {
    int n = getInt();
    vector<long long> l(n);
    for (int i = 0; i < n; i++) {
        cin >> l[i];
    }
    
    map<long long, int> count;
    for (auto x : l) count[x]++;
    
    vector<long long> uniques;
    for (auto &p : count) uniques.push_back(p.first);
    // already sorted because map
    
    if (uniques.empty() || uniques[0] != 0) {
        cout << -1 << "\n";
        return;
    }
    
    long long current = 0;
    long long prev = 0;
    map<long long, long long> val;
    
    for (int i = 0; i < (int)uniques.size(); i++) {
        if (uniques[i] != current) {
            cout << -1 << "\n";
            return;
        }
        
        int m = count[uniques[i]];
        
        long long value;
        if (i == (int)uniques.size() - 1) {
            value = prev + 1;
        } else {
            long long next_s = uniques[i + 1];
            long long diff = next_s - current;
            if (diff % m != 0) {
                cout << -1 << "\n";
                return;
            }
            value = diff / m;
            if (value <= prev) {
                cout << -1 << "\n";
                return;
            }
        }
        
        val[uniques[i]] = value;
        current += (long long)m * value;
        prev = value;
    }
    
    for (int i = 0; i < n; i++) {
        cout << val[l[i]] << (i + 1 == n ? "\n" : " ");
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    int t = 1;
    t = getInt();
    
    for (int _ = 0; _ < t; _++) {
        solve();
    }
    
    return 0;
}