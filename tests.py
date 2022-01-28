import unittest
from dictionary import Dictionary

class TestDictionaryMethods(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestDictionaryMethods, self).__init__(*args, **kwargs)
        self.full_dictionary = Dictionary(['helloworld', 'foo', 'foo', 'bar', 'stylight_team', 'eso', 'oes', '..,'])
        self.empty_dictionary = Dictionary([])

    #  Testing version 1

    def test_find_exsiting_word_v1(self):
        output = self.full_dictionary.find_v1('eso')
        self.assertEqual(len(list(output)), 2)

    def test_find_non_exsiting_word_v1(self):
        output = self.full_dictionary.find_v1('yaaay')
        self.assertEqual(len(list(output)), 0)

    def test_find_empty_input_v1(self):
        output = self.full_dictionary.find_v1('')
        self.assertEqual(len(list(output)), 0)

    def test_find_case_sensitivity_v1(self):
        output = self.full_dictionary.find_v1('ARB')
        self.assertEqual(len(list(output)), 1)

    def test_find_all_punctuation_word_v1(self):
        output = self.full_dictionary.find_v1('.,.')
        self.assertEqual(len(list(output)), 1)

    def test_find_punctuation_word_v1(self):
        output = self.full_dictionary.find_v1('tsylight_team')
        self.assertEqual(len(list(output)), 1)

    def test_find_dublicated_word_v1(self):
        output = self.full_dictionary.find_v1('foo')
        self.assertEqual(len(list(output)), 2)

    def test_find_in_empty_dictionary_v1(self):
        output = self.empty_dictionary.find_v1('foo')
        self.assertEqual(len(list(output)), 0)

    #  Testing version 2

    def test_find_exsiting_word_v2(self):
        output = self.full_dictionary.find_v2('eso')
        self.assertEqual(len(list(output)), 2)

    def test_find_non_exsiting_word_v2(self):
        output = self.full_dictionary.find_v2('yaaay')
        self.assertEqual(len(list(output)), 0)

    def test_find_empty_input_v2(self):
        output = self.full_dictionary.find_v2('')
        self.assertEqual(len(list(output)), 0)

    def test_find_case_sensitivity_v2(self):
        output = self.full_dictionary.find_v2('ARB')
        self.assertEqual(len(list(output)), 1)

    def test_find_all_punctuation_word_v2(self):
        output = self.full_dictionary.find_v2('.,.')
        self.assertEqual(len(list(output)), 1)

    def test_find_punctuation_word_v2(self):
        output = self.full_dictionary.find_v2('tsylight_team')
        self.assertEqual(len(list(output)), 1)

    def test_find_dublicated_word_v2(self):
        output = self.full_dictionary.find_v2('foo')
        self.assertEqual(len(list(output)), 2)

    def test_find_in_empty_dictionary_v2(self):
        output = self.empty_dictionary.find_v2('foo')
        self.assertEqual(len(list(output)), 0)



if __name__ == '__main__':
    unittest.main()