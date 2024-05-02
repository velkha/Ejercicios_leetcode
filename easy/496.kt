class Solution {
    fun nextGreaterElement(nums1: IntArray, nums2: IntArray): IntArray {
        val nextGreater = mutableMapOf<Int, Int>()
        val stack = ArrayDeque<Int>()

        //Vamos revisando elemento a elemento de nums2 y generarmos un diccionario
        //Guardando para cada elemento el cercano mas alto
        for (num in nums2) {
            
            //Vamos guardando el elemento hasta que sea un elemento mas alto y el stack no este acabado asi mismo nos vamos cargando los elementos del stack quue ya no usaremos dado que son valores ya pasados
            while (stack.isNotEmpty() && stack.last() < num) {
                nextGreater[stack.removeLast()] = num
            }
            //Añadimos el elemento al stack
            stack.addLast(num)
        }
        
        while (stack.isNotEmpty()) {
            nextGreater[stack.removeLast()] = -1
        }
        
        return IntArray(nums1.size) { 
            index -> nextGreater[nums1[index]] ?: -1 
        }
    }
}