class Solution(object):
    def maxSubArray(self, nums):
        """
        This solution looks at every possible subarray and returns the maximum.
        It's super inefficient and there must be a better way. Maybe with pointers?

        :type nums: List[int]
        :rtype: int
        """
        
        '''
        1. Check every subarray
        2. Record its sum
        3. If it is the maximum save the subarray
        '''

        max_subarray_sum = 0
        num_elements = len(nums)
        #print(num_elements)

        for subarray_length in range(1, num_elements + 1):
            for i in range(num_elements - subarray_length + 1):
                subarray = nums[i:i+subarray_length]
                #print(i, subarray_length, subarray)
                subarray_sum = sum(subarray)
                if subarray_sum > max_subarray_sum:
                    max_subarray_sum = subarray_sum
            #print('')

        return max_subarray_sum


if __name__ == '__main__':

    
    example_inputs = [[-2,1,-3,4,-1,2,1,-5,4], [1], [5,4,-1,7,8]]
    example_outputs = [6, 1, 23]

    num_problems = len(example_outputs)

    for i in range(num_problems):
        ins = example_inputs[i]
        sol = Solution().maxSubArray(ins)
        expected_output = example_outputs[i]

        print(f'example {i+1} -- {sol == expected_output}. Expected {expected_output} got {sol}')
