function twoSum(numbers: number[], target: number): number[] {
    let auxDic: { [key: number]: number } = {};
    for (let x in numbers) {
        let difference: number = target - numbers[x];
        if (difference in auxDic) {
            return [auxDic[difference]+1, parseInt(x)+1];
        }
        auxDic[numbers[x]] = parseInt(x);
    }
}
/* TRYING TO OPTIMIZE IT */
function twoSum(numbers: number[], target: number): number[] {
    const auxDic: { [key: number]: number } = {};
    for (let i = 0; i < numbers.length; i++) {
        const difference = target - numbers[i];
        if (difference in auxDic) {
            return [auxDic[difference] + 1, i + 1];
        }
        auxDic[numbers[i]] = i;
    }
    throw new Error("No two sum solution");
}