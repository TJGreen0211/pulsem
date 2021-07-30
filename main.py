import unittest


# gian@pulsem.me
# tim@pulsem.me
# do-py


class Replacer(object):
    """
    A class to replace characters in a string.

    Attributes
    ----------
    string : str
        The string that will be modified

    Methods
    -------
    replace(search, replace, indices):
        Replaces characters in a string

    replace_multiple(config):
        Replaces multiple characters in a string based on a config file
    """
    def __init__(self, string):
        self.string = string
        self.indices_replaced = []

    def replace(self, search, replace, indices):
        """Replace n characters in a string
    
        Parameters
        ----------
        search : str
            The character that will be replaced
        replace : str
            The character to replace with
        indices : list
            A list of indices for the positions of the character to be replaced
        """
        found_count = 0
        num_replaced = 0
        char_list = [x for x in self.string]
        for i, c in enumerate(char_list):
            c_lower = c.lower()
            if(c_lower == search):
                if(i not in self.indices_replaced):
                    found_count += 1

                    if(num_replaced == len(indices)):
                        break
                    
                    if(found_count == indices[num_replaced]):
                        num_replaced += 1
                        if c_lower != c:
                            char_list[i] = replace.upper()
                        else:
                             char_list[i] = replace
                        self.indices_replaced.append(i)
        return "".join(char_list)


    def replace_multiple(self, config):
        """Replace n characters in a string multiple times
    
        Parameters
        ----------
        config : list
            List of parameters to be replaced in the form of [('a', 'b', [indices])],
            e.x: config = [
                ('w', 'a', [1, 3]), 
                ('a', 'z', [1, 2, 3])
            ]
        """
        for item in config:
            self.string = self.replace(*item)
        return self.string


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.replacement_string = "Watching whales in Wales, wow."
        self.config = [
            ('w', 'a', [1, 3]), 
            ('a', 'z', [1, 2, 3])
        ]
    
    def test_replace_z(self):
        rep = Replacer(self.replacement_string)
        ret = rep.replace('w', 'z', [2, 3])
        self.assertEqual(ret, "Watching zhales in Zales, wow.")

    def test_replace_a(self):
        rep = Replacer(self.replacement_string)
        ret = rep.replace('a', 'b', [1, 2])
        self.assertEqual(ret, "Wbtching whbles in Wales, wow.")

    def test_replace_multiple(self):
        rep = Replacer(self.replacement_string)
        ret = rep.replace_multiple(self.config)
        self.assertEqual(ret, "Aztching whzles in Azles, wow.")


if __name__ == '__main__':
    unittest.main()
