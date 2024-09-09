/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {number} m
 * @param {number} n
 * @param {ListNode} head
 * @return {number[][]}
 */
var spiralMatrix = function (m, n, head) {
    // let t=new Array(n).fill(-1))
    let mat = new Array(m).fill(-1).map(() => new Array(n).fill(-1));
    let rb = 0, cb = 0, re = m - 1, ce = n - 1;
    // int data;
    while (rb <= re && cb <= ce) {
        for (let i = cb; i <= ce; i++) {
            if (head != null) {
                mat[rb][i] = head.val;
                head = head.next;
            } 
            // else
                // mat[rb][i] = -1;
        }
        rb++;
        for (let i = rb; i <= re; i++) {
            if (head != null) {
                mat[i][ce] = head.val;

                head = head.next;
            }
            //  else
            //     mat[i][ce] = -1;
        }
        ce--;
        if (rb <= re) {

            for (let i = ce; i >= cb; i--) {
                if (head != null) {
                    mat[re][i] = head.val;
                    head = head.next;
                } 
                // else
                //     mat[re][i] = -1;
            }
            re--;
        }
        if (cb <= ce) {

            for (let i = re; i >= rb; i--) {
                if (head != null) {
                    mat[i][cb] = head.val;
                    head = head.next;
                }
                //  else
                //     mat[i][cb] = -1;
            }
            cb++;
        }
    }



    return mat;
};