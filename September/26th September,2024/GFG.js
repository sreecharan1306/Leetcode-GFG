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
        let input_ar1 = readLine().split(' ').map(x => parseInt(x));
        let n = input_ar1.length;
        let a = new Array(n);

        for (let i = 0; i < n; i++) a[i] = input_ar1[i];
        let obj = new Solution();
        console.log(obj.maxStep(a, n));
    }
}
// } Driver Code Ends


// User function Template for javascript

/**
 * @param {number[]} arr
 * @returns {number}
 */

class Solution {
    // Function to find maximum number of consecutive steps
    // to gain an increase in altitude with each step.
    maxStep(arr) {
        // your code here
        let n=arr.length;
        let ans=0;
        let c=0;
        for(let i=1;i<n;i++){
            if(arr[i]>arr[i-1]){
                ans+=1;
            }
            else if(arr[i]<=arr[i-1]){
                ans=0;
            }
            c=Math.max(ans,c);
        }
        return c;
    }
}