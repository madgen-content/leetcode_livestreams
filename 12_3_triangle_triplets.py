
# bad soln, n^3 !
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums = [x for x in list(sorted(nums, reverse = True)) if x !=0]
        i = 0
        accum = 0
        while i < len(nums) - 2:
            x = nums[i]
            j = 1
            while i + j < len(nums)-1:
                y = nums[i+j]
                
                k = 1
                while i+j+k < len(nums):
                    z = nums[i+j+k]
                    if y+z > x:
                        accum += 1
                    k+=1
                j += 1
            i += 1
        return accum

import math
# better soln
# bad soln, n^3 !

def binary_right_heavy_search(arr, start, end, x):

    # end_condition
    if start == end:
        if arr[start] < x:
            return start - 1
        else:
            return start
    
    check = (start + end) // 2
    if arr[check] >= x:
        return binary_right_heavy_search(arr, check + 1, end, x)
    if arr[check] < x:
        return binary_right_heavy_search(arr, start, max(check-1, start), x)
        

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums = [x for x in list(sorted(nums, reverse = True)) if x !=0]


        num_valid_triangles = 0
        for i in range(len(nums) - 2):
            far_right_bound = None
            first_side = nums[i]

            min_second_side = math.ceil(first_side / 2)
            start = i + 1
            end = len(nums) - 2
            rightward_bound = binary_right_heavy_search(nums, start, end, min_second_side)

            for j in range(i+1, rightward_bound+1):
                second_side = nums[j]
                min_third_side = first_side - second_side + 1

                if far_right_bound == None:
                    start = j + 1
                else:
                    start = far_right_bound
                end = len(nums) -1
                far_right_bound = binary_right_heavy_search(nums, start, end, min_third_side)

                num_third_sides = far_right_bound - j
                num_valid_triangles += num_third_sides
        
        return num_valid_triangles


