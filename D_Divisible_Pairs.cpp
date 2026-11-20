
#include <bits/stdc++.h>
using namespace std;

// Type aliases
using ll = long long;
using vi = vector<int>;
using vll = vector<ll>;
using pii = pair<int, int>;

#define all(v) (v).begin(), (v).end()

// Constants
const int MOD = 1e9 + 7;
const int INF = 1e9;
const ll LINF = 1e18;

// Input helpers
int getInt() {
    int x;
    cin >> x;
    return x;
}

ll getLL() {
    ll x;
    cin >> x;
    return x;
}

string getStr() {
    string s;
    cin >> s;
    return s;
}

vi getIntList(int n) {
    vi a(n);
    for (auto &x : a) cin >> x;
    return a;
}

vll getLLList(int n) {
    vll a(n);
    for (auto &x : a) cin >> x;
    return a;
}

template <typename T>
void print(const vector<T>& a) {
    for (int i = 0; i < (int)a.size(); i++) {
        if (i > 0) cout << " ";
        cout << a[i];
    }
    cout << "\n";
}


void solve() {

    int n, x, y; 
    cin >> n >> x >> y;

    vi l = getIntList(n);
    
    int summ = 0;

    map<pair<int, int> ,ll> count;

    ll ans = 0;

    for (auto val : l) {
        int remy = val%y;
        int remx = val % x;

        int need = (x - remx) % x;

        ans += count[{remy, need}];

        count[{remy, remx}]++;
        
    }

    cout << ans << "\n";


}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;
    cin >> t; 

    while (t--) {
        solve();
    }

    return 0;
}
