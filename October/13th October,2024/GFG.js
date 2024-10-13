//{ Driver Code Starts
// Initial Template for javascript

class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

function printList(node) {
    let result = [];
    while (node !== null) {
        result.push(node.data);
        node = node.next;
    }
    console.log(result.join(" "));
}

const readline = require('readline');

const rl = readline.createInterface({input : process.stdin, output : process.stdout});

let inputLines = [];
let currentLine = 0;

rl.on('line', (input) => { inputLines.push(input); });

rl.on('close', () => { main(); });

function readLine() { return inputLines[currentLine++]; }

function main() {
    const t = parseInt(readLine());
    for (let i = 0; i < t; i++) {
        const arr = readLine().split(" ").map(Number);
        let head = new Node(arr[0]);
        let tail = head;
        for (let j = 1; j < arr.length - 1; j++) {
            tail.next = new Node(arr[j]);
            tail = tail.next;
        }
        const ob = new Solution();
        ob.deleteAlt(head);
        printList(head);
    }
}

// } Driver Code Ends


// User function Template for javascript

/*LINKED LIST NODE
class Node {
  constructor(x){
    this.data = x;
    this.next = null;
  }
}
*/

/**
 * @param {Node} head
 */

class Solution {
    deleteAlt(head) {
        // Code here
        let temp=head
        while (temp && temp.next){
            temp.next=temp.next.next
            temp=temp.next
        }
        return head
    }
}
