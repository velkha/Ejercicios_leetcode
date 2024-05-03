class Solution {
    /* Se me ha complicado mas de lo devido, y he acabado teniendo que tirar de Pairs */
    fun dailyTemperatures(temperatures: IntArray): IntArray {
        var intArr = nextGreaterElement(temperatures)
        return intArr
    }
    fun nextGreaterElement(nums1: IntArray): IntArray {
        val stack = ArrayDeque<Pair<Int, Int>>() 
        val newArray = IntArray(nums1.size)
        /* 
        stack.isNotEmpty() && stack.last() 
        nextGreater[stack.removeLast()] 
        stack.addLast(num)*/
        for ((i,num) in nums1.withIndex()) {
            while(stack.isNotEmpty() && stack.last().second < num){
                newArray[stack.last().first] = i - stack.last().first
                stack.removeLast()
            }
            stack.addLast(Pair(i, num))
        }
        return newArray
    }
}