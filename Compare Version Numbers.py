class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        version1 , version2 = version1.split('.') , version2.split('.')

        mx = max(len(version1) , len(version2))

        print(version1 , version2)

        version1 = version1 + ([0]*(mx - len(version1)))

        version2 = version2 + ([0] * (mx - len(version2)))

        i = 0

        while i < mx:

            if int(version1[i]) > int(version2[i]):

                return 1

            elif int(version2[i]) > int(version1[i]):

                return -1

            else:

                i += 1

        return 0
