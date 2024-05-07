/* casi se me va la pinza */
/*function trap(height: number[]): number {
    //REHACERLO DE ZERO HACIENDO QUE EL I PASE POR TODO Y COMPROBANDO LA SUMA BASICA
    //PORQUE SI NO ESTO SE ESTA EMPEZANDO A SOBRECOMPLICAR
   const result: number[][] = [];
    if(height.length <= 1){
        return 0;
    }
    let total:number = 0;
    let auxHeight:number = 0;
    let right:number = 0;

    let auxWater=0;
    console.log(height.length);
    for(let i:number = 0; i<height.length; i++){
        let actualI = height[i];
        console.log("|---"+ i +" - "+ actualI + "---|");
        if(actualI > 0){
            auxWater=0;
            auxHeight=actualI
            console.log("| |***");
            for(let j=actualI;  j>=1; j--){
                right=i+1;
                console.log("| | _____________"+j+" - "+right)
                console.log("| | height[right] "+height[right]);
                //while(right<height.length && height[right]<actualI){
                while(right<height.length && height[right]<=actualI){
                    console.log("| |*** height[right] "+height[right]);
                    console.log("| |*** right "+right);
                    //auxWater+=actualI-height[right];
                    if(height[right]<j){
                        auxWater++;
                    }
                    console.log("| |*** auxWater "+auxWater);
                    right++;
                    console.log("| |****************");
                }
                if(right >= height.length){
                    auxWater=0;
                }
                console.log("| | _____________")
            }
            i=right-1;
            console.log("| |***");
            console.log("| auxWater "+auxWater);
            console.log("| right "+right);
            total+=auxWater;
            console.log("| total "+total);
        }
        console.log("| -------------------------- |")
    }
    console.log("*******************************")
    console.log(total)
    return total;
}; */
/* Otro intento futudo pero este al menos funciona */
/*const result: number[][] = [];
    if(height.length <= 1){
        return 0;
    }
    let total:number = 0;
    let right:number = 0;//height.length-1;
    let left:number = 0;
    let auxWater: number = 0;
    for(let i = 0; i<height.length; i++){
        let actualI = height[i];
        left=i-1;
        right=i+1;
        console.log("| ------ " + i + " - "+actualI)
        while(right<=height.length){
            if(actualI <= height[right]){
                break;
            }
            auxWater+=actualI-height[right];
            right++;
        }
        console.log("right "+right)
        if(right>=height.length){
            auxWater=0;
            if(height[i]>0){
                height[i]--;
                i--;
            }
        }
        
        else{
            i=right-1;
            console.log("RauxWater "+auxWater)
            total+=auxWater;
            auxWater=0;
        }
        console.log("total "+total)
        console.log("| -------")
        
    }
    return total; 
}*/
/* How the fuck i optimize this more actual 800ms, 80ms needed */
function trap(height: number[]): number {
    if (height.length <= 1) {
        return 0;
    }

    let total = 0;
    let left = 0;
    let right = height.length - 1;
    let leftMax = 0;
    let rightMax = 0;

    while (left <= right) {
        console.log("---------------")
        console.log(left, right)
        console.log(height[left], height[right])
        console.log(leftMax, rightMax)
        console.log(total)
        if (height[left] <= height[right]) {
            if (height[left] >= leftMax) {
                leftMax = height[left];
            } else {
                total += leftMax - height[left];
            }
            left++;
        } 
        else //if(height[left] > height[right]) 
        {
            if (height[right] >= rightMax) {
                rightMax = height[right];
            } else {
                total += rightMax - height[right];
            }
            right--;
        }
        console.log(total)
    }

    return total;
};

/** ERA POR CULPA DE LOS LOGS, SIN ELLOS LLEGO A 60MS [Beat 90%] */
function trap(height: number[]): number {
    if (height.length <= 1) {
        return 0;
    }

    let total = 0;
    let left = 0;
    let right = height.length - 1;
    let leftMax = 0;
    let rightMax = 0;

    while (left <= right) {
        if (height[left] <= height[right]) {
            if (height[left] >= leftMax) {
                leftMax = height[left];
            } else {
                total += leftMax - height[left];
            }
            left++;
        } 
        else //if(height[left] > height[right]) 
        {
            if (height[right] >= rightMax) {
                rightMax = height[right];
            } else {
                total += rightMax - height[right];
            }
            right--;
        }
    }

    return total;
};