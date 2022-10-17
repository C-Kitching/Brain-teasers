// Title: Google Kick Start
// Name: Christopher Robert Kitching
// E-mail: christopher.kitching@manchester.ac.uk
// Date created: 17/10/22
// Last editied: 17/10/22
// Description: File to test Leetcode solutions

#include <vector>
#include <iostream>

bool self_dividing(const int& num)
{
    int copy = num;
    while(copy > 0){
        int digit = copy%10;
        if(digit == 0) return false;
        if(num%digit != 0) return false;
        copy /= 10;
    }
    return true;
}

std::vector<int> selfDividingNumbers(const int& left,const int& right) {
    std::vector<int> nums;
    for(int i{left}; i < right + 1; i++){
        if(self_dividing(i)){
            std::cout << i << std::endl;
            nums.push_back(i);
        }
    }
    return nums;
}

int main()
{
    int left = 1; 
    int right = 22;
    std::vector<int> nums = selfDividingNumbers(left, right);


    return 0;
}