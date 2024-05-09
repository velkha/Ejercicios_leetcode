function maxProfit(prices: number[]): number {
    let max: number = 0;
    let min: number = prices[0];
    let actual: number;
    prices.forEach((price) => {
        min = min > price ? price : min;
        actual = price - min;
        max = max < actual ? actual : max;
    });

    return max;
};

/* TRYING TO OPTIMIZE IT */
function maxProfit2(prices: number[]): number {
    let minPrice = Infinity;
    let maxProfit = 0;

    for (let price of prices) {
        if (price < minPrice) {
            minPrice = price;  
        } else if (price - minPrice > maxProfit) {
            maxProfit = price - minPrice;  
        }
    }

    return maxProfit;  
}