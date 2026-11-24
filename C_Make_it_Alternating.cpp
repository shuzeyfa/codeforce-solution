
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

    while (div <= num){
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

    string s; cin >> s;
    int n = (int)s.size();
    int ind = 0;

    ll mod = 998244353;

    vi res;
    int minn = 0;

    while (ind < n){

        int i = ind;
        while (i < n && s[i] == s[ind]){
            i++;
        }
        res.push_back(i - ind);
        minn += (i - ind - 1);
        ind = i;
    }

    ll ans = 1;

    for (auto val : res){
        ans = ans * val % mod;
    }

    for (int i = 2; i<= minn; i++) {
        ans = ans * i % mod;
    }


    
    
    cout << minn << " " << ans << "\n";

    


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
