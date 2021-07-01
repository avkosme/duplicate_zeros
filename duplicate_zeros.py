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



        for zero_key in zero_keys:


            if 1 < zero_key:
                zero_key +=1
            arr.insert(zero_key, 0)

            if len(arr) != len_arr+1:
                del arr[len_arr:]

                break

        self.arr = arr
