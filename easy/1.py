
def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    """creamos un map para poder hacer la busqueda del resultado de target-numactual y si se cumple salimos"""
    aux_dic = {}
    for i, item in enumerate(nums):
        difference = target - item
        if difference in aux_dic:
            return [aux_dic[difference], i]
        aux_dic[item] = i
        #aux_dic[item] = (i, difference)
    return []
    """for key, value in aux_dic.items():
        if value[1] in aux_dic and aux_dic[value[1]][0] != value[0]:
            return aux_dic[key][0], aux_dic[value[1]][0]"""