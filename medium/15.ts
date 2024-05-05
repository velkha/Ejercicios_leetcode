/** Se me ha complicado mas de lo devido pero hacia eones que no usaba este tipo de algoritmo */
function threeSum(nums: number[]): number[][] {
    // Sort the array to use the two-pointer 
    nums.sort((a, b) => a - b);
    const result: number[][] = [];
    for (let i = 0; i < nums.length - 2; i++) {
        if (i > 0 && nums[i] === nums[i - 1]) {
            continue;
        }
        let left = i + 1;
        let right = nums.length - 1;
        // Use two-pointer technique to find the other elements that sum up to zero
        while (left < right) {
            const sum = nums[i] + nums[left] + nums[right];
            if (sum === 0) {
                result.push([nums[i], nums[left], nums[right]]);
                left++;
                right--;
                // Skip duplicate
                while (left < right && nums[left] === nums[left - 1]) {
                    left++;
                }
                while (left < right && nums[right] === nums[right + 1]) {
                    right--;
                }
            } else if (sum < 0) {
                left++;  // Need a larger sum, move the left pointer to the right
            } else {
                right--;  // Need a smaller sum, move the right pointer to the left
            }
        }
    }

    return result;
}