/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
    const arr = nums.sort((a, b) => a - b)
    const end = arr.length
    let ans = []

    for (let i = 0; i < end - 2; i++) {
        if (i > 0 && arr[i] === arr[i - 1]) continue

        let j = i + 1
        let k = end - 1

        while (j < k) {
            const sum = arr[i] + arr[j] + arr[k]
            if (sum == 0) {
                ans.push([arr[i], arr[j], arr[k]])
                while (j < k && arr[j] === arr[j + 1]) j++
                while (j < k && arr[k] === arr[k - 1]) k--
                j++
                k--
            }

            else if (sum > 0)
                k--
            else
                j++
        }

    }

    return ans
};