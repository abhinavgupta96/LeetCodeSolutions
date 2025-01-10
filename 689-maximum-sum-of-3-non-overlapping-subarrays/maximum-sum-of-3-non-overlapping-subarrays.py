class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # n = len(nums)
        # max_sum = float("-inf")
        # result = []

        # for i in range(n-3*k+1) :
        #     for j in range(i+k,(n-2)*k+1):
        #         for l in range(j+k, n-k+1) :
        #             sum1 = sum(nums[i:i+k])
        #             sum2 = sum(nums[j:j+k])
        #             sum3 = sum(nums[l:l+k])
        #             total = sum1 + sum2 + sum3
        #             if total > max_sum:
        #                 max_sum = total
        #                 result = [i,j,l]
        # return result
        n = len(nums)
        window_sum = [0] * (n - k + 1)  # Sum of every k-length window
        current_sum = sum(nums[:k])

        # Calculate all k-length window sums
        for i in range(len(window_sum)):
            if i > 0:
                current_sum += nums[i + k - 1] - nums[i - 1]
            window_sum[i] = current_sum

        # Arrays to track the best index on the left and right
        left = [0] * len(window_sum)
        right = [0] * len(window_sum)

        # Fill left array (max window sum index from the left)
        for i in range(1, len(window_sum)):
            left[i] = i if window_sum[i] > window_sum[left[i - 1]] else left[i - 1]

        # Fill right array (max window sum index from the right)
        right[-1] = len(window_sum) - 1
        for i in range(len(window_sum) - 2, -1, -1):
            right[i] = i if window_sum[i] >= window_sum[right[i + 1]] else right[i + 1]

        # Find the maximum sum of three subarrays
        max_sum = 0
        result = []

        for j in range(k, len(window_sum) - k):
            i = left[j - k]
            l = right[j + k]
            total = window_sum[i] + window_sum[j] + window_sum[l]

            if total > max_sum:
                max_sum = total
                result = [i, j, l]

        return result