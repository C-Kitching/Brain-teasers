def find_lcm(num1, num2):
    if(num1>num2):
        num = num1
        den = num2
    else:
        num = num2
        den = num1
    rem = num % den
    while(rem != 0):
        num = den
        den = rem
        rem = num % den
    gcd = den
    lcm = int(int(num1 * num2)/int(gcd))
    return lcm


def subarrayLCM(nums, k):
        
    count = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            l = nums[i:j+1]
            if len(l) > 1:
                num1 = l[0]
                num2 = l[1]
                lcm = find_lcm(num1, num2)

                for p in range(2, len(l)):
                    lcm = find_lcm(lcm, l[p])

                if lcm == k: count += 1
            else:
                lcm = l[0]
                if lcm == k: count += 1
                
    return count

def main():

    x = [3,6,2,7,1]
    k = 6
    count = subarrayLCM(x, k)
    print(count)

main()