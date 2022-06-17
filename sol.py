class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        ans = 0

        current_sum = sum(arr[:k])

        target = threshold * k

        for i in range(k, len(arr)):

            if current_sum >= target:
                ans += 1

            current_sum = current_sum + arr[i] - arr[i - k]

        if current_sum >= target:
            ans += 1

        return ans