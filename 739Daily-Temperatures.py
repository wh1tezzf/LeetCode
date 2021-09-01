from collections import deque
class Solution:
    def dailyTemperatures(temperatures):
        stack = deque()
        #push first tuple into stack
        stack.append((temperatures[0], 0))
        array = [0] * len(temperatures)
        #each tuple in stack consists of its index and position
        for i in range(1, len(temperatures)):
            if stack:
                nex = (temperatures[i])
                #print(nex)
                element, index = stack.pop()
                while element < nex:
                    array[index] = i - index
                    if len(stack) == 0:
                        break
                
                    element,index = stack.pop()
                
                if element >= nex:
                    stack.append((element, index))
            stack.append((nex, i))
        
        
        return array
        
        
    temperatures = [73,74,75,71,69,72,76,73]
    #temperatures = [75, 71, 69, 72, 76]
    correct = [8,1,5,4,3,2,1,1,0,0]
    print(dailyTemperatures(temperatures))