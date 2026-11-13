class TimeMap:
    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map.setdefault(key, [])
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        arr = self.map[key]
        l, r = 0, len(arr) - 1

        while l <= r:
            m = (l + r) // 2

            if arr[m][0] <= timestamp:
                l = m + 1
            else:
                r = m - 1

        if r == -1:
            return ""
        else:
            return arr[r][1]
