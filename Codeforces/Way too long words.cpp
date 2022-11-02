#include <iostream>
#include <string>

using namespace std;

int main()
{
    std::string s;
    int n;

    cin >> n;
    for(int i{0}; i < n; i++){
        cin >> s;

        if(s.size() <= 10) cout << s << "\n";
        else{
            cout << s.front() << s.size() - 2 << s.back() << "\n";
        }
    }

    return 0;
}