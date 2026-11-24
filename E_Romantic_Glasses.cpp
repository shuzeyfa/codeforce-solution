
#include <bits/stdc++.h>
using namespace std;

// Type aliases
using ll = long long;
using vi = vector<int>;
using vll = vector<ll>;
using pii = pair<int, int>;

#define all(v) (v).begin(), (v).end()
#define rall(x) (x).rbegin(), (x).rend()
#define bisect_left(v, x) (int)(lower_bound((v).begin(), (v).end(), (x)) - (v).begin())
#define bisect_right(v, x) (int)(upper_bound((v).begin(), (v).end(), (x)) - (v).begin())

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

template <typename Container>
void print(const Container& a) {
    for (const auto& x : a) {
        cout << x << " ";
    }
    cout << "\n";
}


void solve() {

    int n = getInt();
    vi l = getIntList(n);

    set<ll> seen;
    seen.insert(0);
    ll summ = 0;
    // print(seen);
    for (int i=0; i < n; i++){
        if (i%2 == 0){
            summ += l[i];
        }else{
            summ -= l[i];
        }

        if (seen.count(summ) > 0){
            cout << "YES\n" ;
            return;
        }
        seen.insert(summ);
    }
    // print(seen);
    cout << "NO\n";

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
