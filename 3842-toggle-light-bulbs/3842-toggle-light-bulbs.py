class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        on = set()
        
        for bulb in bulbs:
            on ^= {bulb}
        
        return sorted(on)