class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set()
        adjList = defaultdict(set)
        def FindWordDiff(word1, word2):
            diff = 0
            if len(word1) != len(word2) or word1==word2:
                return False
            for i in range(len(word1)):
                if word1[i]!=word2[i]:
                    diff += 1
                    if diff > 1:
                        return False
            return True

        if endWord not in wordList:
            return 0
        wordList.append(beginWord)  
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i]+'*'+word[i+1:]
                adjList[pattern].add(word)
        
        
        
        visited = set()
        my_q = deque()
        my_q.append(beginWord)
        visited.add(beginWord)
        curr_level = 0
        while my_q:
            curr_size = len(my_q)
            curr_level += 1
            for i in range(curr_size):
                curr_word = my_q.popleft()
                for i in range(len(curr_word)):
                    pattern = curr_word[:i]+'*'+curr_word[i+1:]
                    for next_word in adjList[pattern]:
                        if next_word not in visited:
                            my_q.append(next_word)
                            visited.add(next_word)
                            if next_word == endWord:
                                return curr_level+1
        return 0