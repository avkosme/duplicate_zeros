class Solution:

    arr = []

    def duplicateZeros(self, arr: [int]) -> None:

        len_arr = len(arr)

        k = 0
        zero_keys = []
        for val in arr:

            if val == 0:
                zero_keys.append(k)

            k += 1

        k = 0
        for zero_key in zero_keys:

            zero_key = k + 1 + zero_key
            arr.insert(zero_key, 0)

            k +=1

        self.arr = arr[:len_arr]
