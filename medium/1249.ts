function minRemoveToMakeValid(s: string): string {
    let openCount = 0;
    let sArr = s.split('');
    for (let i = 0; i < sArr.length; i++) {
        if (sArr[i] === '(') {
            openCount++;
        } else if (sArr[i] === ')') {
            if (openCount === 0) {
                sArr[i] = '';
            } else {
                openCount--;
            }
        }
    }
    let closeCount = 0;
    for (let i = sArr.length - 1; i >= 0; i--) {
        if (sArr[i] === ')') {
            closeCount++;
        } else if (sArr[i] === '(') {
            if (closeCount === 0) {
                sArr[i] = '';
            } else {
                closeCount--;
            }
        }
    }
    return sArr.join('');
};