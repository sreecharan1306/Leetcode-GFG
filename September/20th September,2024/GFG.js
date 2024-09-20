//{ Driver Code Starts
// Initial Template for javascript

const readline = require('readline');
const rl = readline.createInterface({input : process.stdin, output : process.stdout});

let inputLines = [];
let currentLine = 0;

rl.on('line', function(line) { inputLines.push(line); });

rl.on('close', function() {
    let t = parseInt(inputLines[currentLine++]);
    for (let i = 0; i < t; i++) {
        let height = inputLines[currentLine++].split(' ').map(Number);
        let ob = new Solution();
        let ans = ob.countBuildings(height);
        console.log(ans);
    }
});

// } Driver Code Ends


// User function Template for javascript

/**
 * @param {number[]} height
 * @returns {number}
 */

class Solution {
    // Returns count buildings that can see sunlight
    countBuildings(height) {
        // code here
        let max=height[0];
        let ans=1;
        for(let i=1;i<height.length;i++){
            if(height[i]>max){
                ans++;
                max=height[i];
            }
        }
        return ans;
        
    }
}
