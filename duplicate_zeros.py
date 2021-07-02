class Solution:

    arr = []

    def duplicateZeros(self, arr: [int]) -> None:

        len_arr = len(arr)

        zero_keys = []
        for k, val in enumerate(arr):

            if val == 0:
                zero_keys.append(k)

            k += 1


        for k_zero, zero_key in enumerate(zero_keys):

            zero_key = k_zero + 1 + zero_key
            arr.insert(zero_key, 0)
            del arr[-1]

            k_zero +=1

        self.arr = arr
