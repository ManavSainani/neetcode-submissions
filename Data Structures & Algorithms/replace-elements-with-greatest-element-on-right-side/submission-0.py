class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #steps
        #1. initial max = -1
        #2. iterate in reverse order (R to L)
        #3. new max = max(oldmax, arr[i])
        
        max_val = -1

        for i in range(len(arr) - 1, -1, -1):
            newMax = max(max_val, arr[i])
            arr[i] = max_val
            max_val = newMax
        return arr
