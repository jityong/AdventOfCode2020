class Day9:
    # Part 1 -> O(N^2), where N is the total number of values
    # Part 2 -> O(K), where K is the size of the window
    def find_invalid_number(self, arr, window_size):
        def is_in_window(window, target):
            for num in window:
                other_num = target - num
                if other_num != num and other_num in window:
                    return True 
            return False

        l,r = 0, window_size
        window = set(arr[:window_size])
        while r < len(arr):
            if not is_in_window(window, arr[r]):
                return arr[r]
            window.remove(arr[l])
            window.add(arr[r])
            l += 1
            r += 1
        return -1

    def sliding_window(self, arr, target):
        l,r = 0,0
        window = 0
        while r < len(arr):
            window += arr[r]
            while window > target and l < r:
                window -= arr[l]
                l += 1
            if window == target:
                if r - l == 1:
                    window -= arr[l]
                    l += 1
                else:
                    return (l,r)
            r += 1
        return (-1,-1)    
    
    def find_smallest_and_largest(self, arr, target):
        l,r = self.sliding_window(arr, target)
        smallest_val = 1e10
        largest_val = 0
        for i in range(l, r+1):
            smallest_val = min(smallest_val, arr[i])
            largest_val = max(largest_val, arr[i])
        return (smallest_val, largest_val)

lines = open("../inputs/day9input.txt", "r+")
arr = lines.read().splitlines()

arr = list(map(lambda x: int(x), arr))
day9 = Day9()
target = day9.find_invalid_number(arr, 25)
print(target)

smallest_val, largest_val = day9.find_smallest_and_largest(arr,target)
print(smallest_val + largest_val)


