/*
 * @lc app=leetcode id=202 lang=typescript
 *
 * [202] Happy Number
 */

// @lc code=start
function isHappy(n: number): boolean {
    if (n === 0) return false;

    // hardcoding
    while (n != 1 && n != 4) {

        let sumOfNumber: number = 0
        let dividedNum: number = n

        // 割り続けたらdividedNumは<0
        while (dividedNum > 0) {

            sumOfNumber += (dividedNum % 10) * (dividedNum % 10);
            dividedNum = Math.floor(dividedNum / 10)

        }

        n = sumOfNumber
    }

    return n == 1
};
// @lc code=end

