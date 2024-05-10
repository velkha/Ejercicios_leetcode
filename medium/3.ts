/* first solution */ 
function lengthOfLongestSubstring(s: string): number {
    let count: number = 0;
    let max: number = 0;
    let dict: { [key: string]: number } = {};
    let newStart = 0;
    for(let i = 0; i < s.length; i++){
        if(dict[s[i]] != null){
            newStart = newStart > dict[s[i]] ? newStart : dict[s[i]];
            count = i-newStart;
            dict[s[i]] = null
        }
        count++;
        if(count > max) max = count;
        dict[s[i]] = i+1;
    }
    return max;
};

/* Second try, same performance */
function lengthOfLongestSubstring(s: string): number {
    let max: number = 0;
    let dict: { [key: string]: number } = {};
    let start: number = 0; 

    for (let i = 0; i < s.length; i++) {
        let char = s[i];
        if (dict[char] !== undefined && dict[char] >= start){
            start = dict[char] + 1; 
        }
        dict[char] = i;
        max = Math.max(max, i - start + 1); 
    }

    return max;
}

/* Not mine, but slightly faster (like 5-10% faster), interesting use of scanner*/ 
function lengthOfLongestSubstring(s: string): number {
    const scanner: string[] = []
    let longest = 0
  
    for (const char of s) {
      const possibleIndex = scanner.indexOf(char)
  
      if (possibleIndex !== -1) { scanner.splice(0, possibleIndex + 1) }
      scanner.push(char)
      longest = Math.max(longest, scanner.length)
    }
  
    return longest
  }