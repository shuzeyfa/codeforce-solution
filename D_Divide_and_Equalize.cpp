
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

vi fact(int num){

    int div = 2;
    vi factors;

    while (div*div <= num){
        while (num%div == 0){
            factors.push_back(div);
            num /= div;
            
        }
        div += 1;
    }
    if (num > 1){
        factors.push_back(num);
    }
    return factors;
}

void solve() {

    int n = getInt();
    vi l = getIntList(n);


    map<int, int> d;

    for (int i=0; i < n; i++) {
        vi val = fact(l[i]);
        for (auto value : val){
            d[value]++;
        }
    }

    for (auto [key, value] : d){
        if (value%n != 0){
            cout << "NO\n";
            return;
        }
    }
    cout << "YES\n";


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
