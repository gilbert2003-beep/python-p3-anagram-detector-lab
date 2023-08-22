# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        result = []
        for candidate in word_list:
            if self.is_anagram(candidate):
                result.append(candidate)
        return result

    def is_anagram(self, candidate):
        return sorted(candidate.lower()) == sorted(self.word.lower()) and candidate.lower() != self.word.lower()
