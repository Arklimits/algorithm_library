/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (arr, target) {
    const map = {}

    for (let i = 0; i < arr.length; i++) {
        const t = target - arr[i]
        if  (t in map) 
            return [map[t], i]
        
        map[arr[i]] = i
    }
    return
};