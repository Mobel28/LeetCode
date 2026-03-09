class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        seen_one=False
        segment_ended=False
        for ch in s:
            if ch=='1':
                if segment_ended:
                    return False
                seen_one=True
            else:
                if seen_one:
                    segment_ended=True
        return True