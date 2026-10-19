#include <bits/stdc++.h>
using namespace std;

// ============================================
// 1. BASIC I/O  (Python: print / input)
// ============================================
int main() {
    // Fast I/O (very important for CP to avoid TLE)
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // Output
    cout << "Hello, world!" << "\n";

    // Input
    int x;
    cin >> x;                    // single integer
    // string s; cin >> s;       // single word
    // string line; getline(cin, line);  // whole line

    // Multiple inputs on one line
    int a, b;
    cin >> a >> b;

    return 0;
}

// ============================================
// 2. VARIABLES & DATA TYPES
// ============================================
/*
Python:
x = 4
x = "A2SV"
*/

void variables() {
    int x = 4;                  // integer
    long long big = 1e18;       // use this for large numbers (very common in CP)
    double d = 3.14;            // floating point
    string s = "A2SV";          // string
    bool flag = true;           // true / false

    // Dynamic typing does NOT exist in C++
    // You must declare the type
}

// ============================================
// 3. OPERATORS (same as Python almost)
// ============================================
void operators() {
    int x = 10, y = 3;

    cout << x + y << "\n";   // 13
    cout << x - y << "\n";   // 7
    cout << x * y << "\n";   // 30
    cout << x / y << "\n";   // 3   (integer division)
    cout << x % y << "\n";   // 1

    // Floor division in C++ is just / for positive numbers
    // Power: use pow() from <cmath> or write your own loop

    // Comparison
    cout << (x == y) << "\n";  // 0 (false)
    cout << (x != y) << "\n";  // 1 (true)
    cout << (x > y)  << "\n";  // 1
    cout << (x < y)  << "\n";  // 0
    cout << (x >= y) << "\n";  // 1
    cout << (x <= y) << "\n";  // 0

    // Logical
    cout << (x > 5 && y < 5) << "\n";  // and
    cout << (x > 5 || y > 5) << "\n";  // or
    cout << !(x == y) << "\n";         // not
}

// ============================================
// 4. CONDITIONALS
// ============================================
void conditionals() {
    int x = 10;

    if (x > 0) {
        cout << "Positive\n";
    } else if (x == 0) {
        cout << "Zero\n";
    } else {
        cout << "Negative\n";
    }

    // Ternary (short if)
    string result = (x > 0) ? "Positive" : "Not positive";
}

// ============================================
// 5. LOOPS
// ============================================
void loops() {
    // for loop (most common in CP)
    for (int i = 0; i < 5; i++) {
        cout << i << " ";
    }
    cout << "\n";

    // while
    int i = 0;
    while (i < 5) {
        cout << i << " ";
        i++;
    }
    cout << "\n";

    // range-based for (like Python "for x in list")
    vector<int> v = {10, 20, 30};
    for (int num : v) {
        cout << num << " ";
    }
    cout << "\n";

    // with index
    for (int i = 0; i < (int)v.size(); i++) {
        cout << i << " " << v[i] << "\n";
    }
}

// ============================================
// 6. FUNCTIONS
// ============================================
int add(int a, int b) {
    return a + b;
}

void printHello() {
    cout << "Hello\n";
}

void functions_demo() {
    cout << add(3, 5) << "\n";   // 8
    printHello();
}

// ============================================
// 7. LISTS  →  vector  (most important for CP)
// ============================================
/*
Python:
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
fruits[0] = "orange"
fruits.pop()
*/

void lists_as_vectors() {
    vector<int> nums = {10, 11, 12, 13, 14};

    // Access
    cout << nums[0] << "\n";      // first
    cout << nums.back() << "\n";  // last

    // Size
    cout << nums.size() << "\n";

    // Append
    nums.push_back(15);

    // Remove last
    nums.pop_back();

    // Insert at position
    nums.insert(nums.begin() + 1, 99);  // insert 99 at index 1
    // Remove by value (find first then erase)
    auto it = find(nums.begin(), nums.end(), 12);
    if (it != nums.end()) nums.erase(it);

    // Sort
    sort(nums.begin(), nums.end());           // ascending
    sort(nums.rbegin(), nums.rend());         // descending

    // Reverse
    reverse(nums.begin(), nums.end());

    // Check if exists
    if (find(nums.begin(), nums.end(), 10) != nums.end()) {
        cout << "Found\n";
    }

    // Slice equivalent (create new vector)
    // nums[2:5] → 
    vector<int> sub(nums.begin() + 2, nums.begin() + 5);
}

// ============================================
// 8. TUPLES  →  pair  (or tuple for more than 2)
// ============================================
void pairs_and_tuples() {
    // Simple pair (very common in CP)
    pair<int, int> p = {3, 5};
    cout << p.first << " " << p.second << "\n";

    // pair of string and int
    pair<string, int> student = {"John", 36};

    // More than 2 values
    tuple<int, string, double> t = {1, "A2SV", 3.14};
    cout << get<0>(t) << " " << get<1>(t) << "\n";
}

// ============================================
// 9. SETS
// ============================================
/*
Python:
my_set = {1, 2, 3}
my_set.add(4)
*/

void sets_demo() {
    set<int> s;                 // ordered set (sorted, unique)
    // unordered_set<int> s;    // faster, unordered (use when order doesn't matter)

    s.insert(1);
    s.insert(2);
    s.insert(3);
    s.insert(2);                // ignored (unique)

    // Check existence
    if (s.count(2)) cout << "Exists\n";

    // Remove
    s.erase(2);

    // Iterate
    for (int x : s) cout << x << " ";
    cout << "\n";

    // Size
    cout << s.size() << "\n";
}

// ============================================
// 10. DICTIONARIES  →  map / unordered_map
// ============================================
/*
Python:
d = {"name": "John", "age": 36}
d["age"] = 37
*/

void maps_demo() {
    map<string, int> mp;                    // ordered by key
    // unordered_map<string, int> mp;       // faster (use this most of the time in CP)

    mp["name"] = 1;          // just example, value is int here
    mp["age"] = 36;

    // Access / update
    mp["age"] = 37;

    // Check if key exists
    if (mp.count("age")) {
        cout << mp["age"] << "\n";
    }

    // Iterate
    for (auto& [key, value] : mp) {         // C++17
        cout << key << " " << value << "\n";
    }
    // or older style:
    // for (auto it = mp.begin(); it != mp.end(); ++it)
    //     cout << it->first << " " << it->second << "\n";
}

// ============================================
// 11. STRINGS (very common)
// ============================================
void strings_demo() {
    string s = "hello";
    cout << s.size() << "\n";
    cout << s[0] << "\n";           // 'h'
    s += " world";                  // concatenate
    cout << s.substr(0, 5) << "\n"; // "hello"
}

// ============================================
// 12. COMMON CP PATTERNS
// ============================================
void common_patterns() {
    // Read n numbers into vector
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    // Sum
    long long sum = 0;
    for (int x : a) sum += x;

    // Find max / min
    int mx = *max_element(a.begin(), a.end());
    int mn = *min_element(a.begin(), a.end());

    // Frequency count
    map<int, int> freq;
    for (int x : a) freq[x]++;
}
