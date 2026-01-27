class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):  # Use 32 iterations to handle all 32 bits
            result <<= 1  # Shift result to the left by 1 to make space for the next bit
            result |= (n & 1)  # Add the last bit of n to result
            n >>= 1  # Shift n to the right by 1 to process the next bit
        return result

        