
class SpeSkillTest():
    
    def __init__(self):
        pass
    
    def narcissistic(self, input_number):
        power = len(str(input_number))
        a = list(int(str(input_number)[i]) for i in range(power))
        sum = 0
        for i in a:
            sum += i**power
        if sum == input_number: return("true") 
        else: return("false")
        
    def parity_outlier(self, input_list):
        even_list = []
        odd_list = []
        for i in input_list:
            if i % 2 > 0:
                odd_list.append(i)
            if i % 2 == 0:
                even_list.append(i)
        if len(even_list) == 1:
            return even_list[0]
        elif len(odd_list) == 1:
            return odd_list[0]
        else:
            return('false')
        
    def findNeedle(self, haystack, needle):        
        return(haystack.index(needle))
    
    def blueOcean(self, integer_list, exclude_list):
        copy_set = set(i for i in integer_list)
        for i in exclude_list:
            copy_set.remove(i)
        return(list(copy_set))
        
number = SpeSkillTest()
        