class Solution:
    def isPossible(self, arr, s, x):
        # Generate the sequence
        sequence = [s]
        total = s
        
        for num in arr:
            next_num = total + num
            sequence.append(next_num)
            total += next_num
        
        # Check if x can be formed
        # Since each number is greater than sum of all previous (because arr[i] >= 1),
        # we can use greedy approach from largest to smallest
        for i in range(len(sequence) - 1, -1, -1):
            if x >= sequence[i]:
                x -= sequence[i]
        
        return x == 0