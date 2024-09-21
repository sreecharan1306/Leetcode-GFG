/**
 * @param {number} n
 * @return {number[]}
 */
var lexicalOrder = function(n) {

    // Approach 1
    let arr=[]
    for(let i=0;i<n;i++) arr.push(i+1)
    return arr.sort()
    
    // Approach 2 by llama3
    // return [...Array(n).keys()].map(i => i + 1).sort();

};