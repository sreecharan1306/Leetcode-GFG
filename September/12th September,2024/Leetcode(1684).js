/**
 * @param {string} allowed
 * @param {string[]} words
 * @return {number}
 */
var countConsistentStrings = function (allowed, words) {
    let s = new Set(allowed)
    let ans = 0
    for (let i = 0; i < words.length; i++) {
        let flag = true;
        const w = words[i];
        for (let j = 0; j < w.length; j++) {
            const ch = w[j]
            if (!s.has(ch)) {
                flag = false;
                break
            }
        }
        if (flag) ans++;
    }
    return ans;
};