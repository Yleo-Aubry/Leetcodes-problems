class Solution(object):
    def searchMatrix(self, matrix, target):

         """

        :type matrix: List[List[int]]

        :type target: int

        :rtype: bool

        """
         if not matrix: 
             return False
        
         ROWS, COLS = len(matrix), len(matrix[0])
        
         l, r = 0, (ROWS * COLS) - 1
        
         while l <= r:
             mid = (l + r) // 2
            
             r_pos = mid // COLS
             c_pos = mid % COLS
            
             val = matrix[r_pos][c_pos]
            
             if val > target:
                 r = mid - 1
             elif val < target:
                 l = mid + 1
             else:
                 return True
                
         return False
