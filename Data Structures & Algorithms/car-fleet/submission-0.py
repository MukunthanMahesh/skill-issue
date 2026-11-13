class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        ahead = 0

        st = []
        for pos, spd in cars:
            time = (target - pos) / spd
            if not st or time > st[-1]:
                st.append(time)
        return len(st)