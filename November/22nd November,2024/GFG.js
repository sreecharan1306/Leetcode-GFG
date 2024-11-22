//{ Driver Code Starts
// Initial Template for javascript
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => { inputString += inputStdin; });

process.stdin.on('end', _ => {
    inputString =
        inputString.trim().split('\n').map(string => { return string.trim(); });

    main();
});

function readLine() { return inputString[currentLine++]; }

function main() {
    let t = parseInt(readLine());
    let i = 0;
    for (; i < t; i++) {
        let prices = new Array();
        let input_ar1 = readLine().split(' ').map(x => parseInt(x));
        for (let i = 0; i < input_ar1.length; i++) prices.push(input_ar1[i]);
        let obj = new Solution();
        let res = obj.maximumProfit(prices);
        console.log(res);
        console.log("~");
    }
}
// } Driver Code Ends


// User function Template for javascript
/**
 * @param {number[]} prices
 * @returns {number}
 */

class Solution {
    // Function to find the maximum profit.
    maximumProfit(prices) {
        // your code here
        let ans=0
        let m=100000
        for(let i=0;i<prices.length;i++){
            m=Math.min(m,prices[i])
            ans=Math.max(ans,prices[i]-m)
        }
        return ans;
    }
}