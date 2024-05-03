class Solution {
    /* Se me ha complicado mas de lo devido, y he acabado teniendo que tirar de Pairs */
    /* Version antigua, consumiendo un poco mas de memoria de la devida
    fun dailyTemperatures(temperatures: IntArray): IntArray {
        val stack = ArrayDeque<Pair<Int, Int>>() 
        val newArray = IntArray(temperatures.size)
        for ((i,num) in temperatures.withIndex()) {
            while(stack.isNotEmpty() && stack.last().second < num){
                newArray[stack.last().first] = i - stack.last().first
                stack.removeLast()
            }
            stack.addLast(Pair(i, num))
        }
        return newArray
    }*/
    // Version mejorada con una pizca de memoria menos pero la diferencia es minima
    fun dailyTemperatures(temperatures: IntArray): IntArray {
        val stack = ArrayDeque<Int>()
        val newArray  = IntArray(temperatures.size)
        for (index in temperatures.indices) {
            while (stack.isNotEmpty() && temperatures[stack.last()] < temperatures[index]) {
                val prevIndex = stack.removeLast()
                newArray [prevIndex] = index - prevIndex
            }
            stack.addLast(index)
        }
        return newArray 
    }

}