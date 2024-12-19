/**
 * @param {number[]} arr
 * @return {number}
 */
var maxChunksToSorted = function(arr) {
    let ans=0;
    let m=0;
    for(let i=0;i<arr.length;i++){
        m=Math.max(arr[i],m);
        if(m<=i) ans++;
    }
    return ans;
};