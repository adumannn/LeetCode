class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        # target int array
        # int n
        # stream of int [1, n]
        # if the stream is not empty,
        # s = [target[0]]
        s = []
        res = []
        # 1 2 3
        
        for i in range(1, n+1):  # 1 2 3
            # print(i)
            if s == target:
                break
            if i not in target:  #  i =1 2 3 # target = 1, 3
                s.append(i)
                s.pop()
                res.append("Push")
                res.append("Pop")
            else:
                s.append(i)
                res.append("Push")

        return res