
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

template <typename T>
void print(const vector<T>& a) {
    for (int i = 0; i < (int)a.size(); i++) {
        if (i > 0) cout << " ";
        cout << a[i];
    }
    cout << "\n";
}


void solve() {

    int n = getInt();
    vi l = getIntList(n);

    vi loc;
    loc.push_back(0);

    vi normal;
    normal.push_back(0);

    for (int i = 1; i < n; i++) {
        if (l[i] != l[i-1]) {
            loc.push_back(i);
            normal.push_back(i);
        } else {
            normal.push_back(normal.back());
        }
    }

    int q; cin >> q;

    for (int i=0; i < q; i++){
        int left, right;
        cin >> left >> right;
        int index = normal[left-1];

        int index2 = bisect_left(loc, index);
        if (index2 + 1 == (int)loc.size() || loc[index2+1] >= right){
            cout << -1 << " " << -1 << '\n';
        }else{
            cout << left << " " << loc[index2+1] + 1 << '\n';
        }
    }
    cout << '\n';

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
