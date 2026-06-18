class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        m_ngle = 6.0 * minutes

        val = hour % 12

        h_ngle = 30.0 * val + 0.5 * minutes

        ans = abs(h_ngle - m_ngle)

        return min(ans , 360.0 - ans)

        
