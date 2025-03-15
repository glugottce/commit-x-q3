#include <iostream>
#include <vector>

using namespace std;

int findSingleNumber(vector<int>& nums) {
    int single = 0;
    
    
    for (int num : nums) {
        single ^= num;
    }
    
    return single;
}

int main() {
    int n;
    cin >> n;

    vector<int> nums(n);
    cout  << n << endl;

    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    cout << findSingleNumber(nums) << endl;

    return 0;
}
