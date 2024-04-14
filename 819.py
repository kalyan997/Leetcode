class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        words = re.findall(r'\w+', paragraph.lower())
        #words = [re.sub(r'[.,!]', '', word) for word in words]
        max_freq = 0
        max_word = ""
        word_freq = defaultdict(int)
        banned_words = set(banned)
        print(words)
        #print(banned_words)
        for word in words:
            word = word.lower()
            word_freq[word] += 1
            if word not in banned_words:
                if word_freq[word] > max_freq:
                    max_freq = word_freq[word]
                    max_word = word
        print(word_freq)
        return max_word