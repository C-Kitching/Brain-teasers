#include <iostream>

using namespace std;

int main()
{
    long long n, m;
    int a;
    long long res;

    cin >> n >> m >> a;

    if(n%a == 0){
        if(m%a ==0){
            res = (n/a)*(m/a);
        }
        else{
            res = ((n/a)*(m/a + 1));
        }
    }
    else if(m%a == 0){
        res = ((n/a + 1)*(m/a));
    }
    else{
        res = (n/a + 1)*(m/a + 1);
    }

    cout << res;

    return 0;
}