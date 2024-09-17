/**
 * @param {string} s1
 * @param {string} s2
 * @return {string[]}
 */
var uncommonFromSentences = function(s1, s2) {
    let a=[...s1.split(" "),...s2.split(' ')]
    let ans=[]
    let b={}
    console.log(a)
    let d=new Map();
    for(let i of a){
        if(i in b) b[i]+=1
        else b[i]=1
    }
    for(let i in b){
        if(b[i]==1) ans.push(i)
    }
    return ans
};