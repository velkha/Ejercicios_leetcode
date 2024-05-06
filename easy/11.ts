/* FIRST VERSION - no he podido optimizarla mas, y ya esta > 90% */
function maxArea(height: number[]): number {
    const result: number[][] = [];
    if(height.length <= 1){
        return 0;
    }
    let maxArea:number = 0;
    let left:number = 0;
    let right:number = height.length-1;
    while(left < right) {
        let actHeight:number = height[left] < height[right]? height[left] : height[right];
        let actArea:number = (right-left)*actHeight;
        if(maxArea < actArea){
            maxArea=actArea;
        }
        if(height[left] > height[right]){
            right--;
        }
        else{
            left++;
        }
    }
    return maxArea;
};