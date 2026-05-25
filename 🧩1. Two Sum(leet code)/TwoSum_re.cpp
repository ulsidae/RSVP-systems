#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;

        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];

            // Check if the complement already exists
            if (seen.find(diff) != seen.end()) {
                return {seen[diff], i};
            }

            // Store current value with its index
            seen[nums[i]] = i;
        }

        return {};
    }
};