class Dictionary:
 
    def __init__(self, dictionary_content):
        self.dictionary_content = dictionary_content

    def find_v1(self, word_to_find):
        """
            Approach in points:
            - construct a sorted list out of word_to_find
            - loop over the list of words, check if:
                * 2 words have the same length
                * 2 sorted lists are the same 
            pros:
            - linear space complexity
            - len(word) ==  n eliminates sorting a word that does not match the criteria 
            cons:
            - slower solution 
        """
        word_to_find = sorted(word_to_find.lower())
        n = len(word_to_find)

        for word in self.dictionary_content:
            if len(word) ==  n and word_to_find == sorted(word.lower()):
                yield word


# Time Complexity = O(nmlogm)
# where n = lenght of list (dictionary content) and m = average length of words in the list 
# Space complexity = O(1)

    @staticmethod
    def hash_word(word):
        """
            A helper function to hash a string
            input: word to be hashed
            outptu: hashmap of words

            This function can be replaced by using Counter.count(). However, it was implemented to eliminate the usage of any other dependencies 
        """
        word_hashed = {}
        for char in word:
            word_hashed[char] = word_hashed.get(char, 0) + 1

        return word_hashed

    def find_v2(self, word_to_find):
        """
            Approach in points:
            - construct a hashmap out of word_to_find
            - loop over the list of words and compare the has of word_to_find and the worx in the list
            - if 2 hashmap are the same it means same content and same len
            pros:
            - faster solution 
            cons:
            - space complexity affected by the average length of words 

        """
        word_to_find_hashed = Dictionary.hash_word(word_to_find.lower())

        for word in self.dictionary_content:
            if word_to_find_hashed == Dictionary.hash_word(word.lower()):
                yield word

# Time Complexity = O(nm)
# where n = lenght of list (dictionary content) and m = average length of words in the list 
# Space complexity = O(m) where m = average length of words in the list 


# Can both complexity be optimised? well, this is a question that i would never say No to, 
# but keeping it simple straight forward i believe this is a good solution 

# the 2 provided solution are valid depending on what you need to achieve for example, in case of 
# number of “find” requests gets extremely large you would prefer to go for the faster approach. However, 
# in case of size of the initial string list is very large it is better to go for teh solution that 
# optimizies tha space complexity 