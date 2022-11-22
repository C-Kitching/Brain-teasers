#include<vector>
#include<iostream>
#include<algorithm>

using namespace std;

int main()
{
    int T, N, L, D, laps;
    char C;
    
    cin >> T;
    for(int i{0}; i < T; i++){
        cin >> L >> N;
        
        laps = 0;
        int a_sum = 0;
        int c_sum = 0;

        for(int j{0}; j < N; j++){
            cin >> D >> C;

            if(C == 'A') a_sum += D;
            else c_sum += D;
        }

        laps += abs(a_sum/L) + abs(c_sum/L);
        
        cout << "Case #" << i+1 << ": " << laps << "\n";
        
    }

    return 0;
}