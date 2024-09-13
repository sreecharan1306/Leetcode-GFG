/**
 * @param {number[]} arr
 * @param {number[][]} queries
 * @return {number[]}
 */
var xorQueries = function(arr, queries) {
    let temp=[arr[0]]
    let n=arr.length;
    let ans=[]
    for(let i=1;i<n;i++){
        temp.push(temp[i-1]^arr[i])
    }
    for(let i=0;i<queries.length;i++){
        let a=queries[i][0]
        let b=queries[i][1]
        if(a==0) ans.push(temp[b])
        else ans.push(temp[b]^temp[a-1])
    }
    return ans;

};