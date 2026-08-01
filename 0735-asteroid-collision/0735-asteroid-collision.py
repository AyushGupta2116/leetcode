class Solution(object):
    def asteroidCollision(self, arr):
        changed = 1

        while changed:
            changed = 0
            i = 0

            while i < len(arr) - 1:

                if arr[i] > 0 and arr[i + 1] < 0:

                    if abs(arr[i]) > abs(arr[i + 1]):
                        arr = arr[:i + 1] + arr[i + 2:]

                    elif abs(arr[i]) < abs(arr[i + 1]):
                        arr = arr[:i] + arr[i + 1:]

                    else:
                        arr = arr[:i] + arr[i + 2:]

                    changed = 1
                    break

                i += 1

        return arr