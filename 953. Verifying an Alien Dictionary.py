from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words) - 1):
            flag = True
            for j in range(min(len(words[i]), len(words[i + 1]))):
                if order.find(words[i + 1][j]) < order.find(words[i][j]):
                    return False
                if order.find(words[i + 1][j]) > order.find(words[i][j]):
                    flag = False
                    break
            if len(words[i]) > len(words[i + 1]) and flag:
                return False
        return True
