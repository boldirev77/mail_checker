"""
    File name: 
    Author: Aleksander Boldyrev
    Python Version: 3.3
"""

import unittest
from ismail import ismail


class IsmailTest(unittest.TestCase):

    # checking cond_a - '@' should be present in the mail and only once
    def test_cond_a(self):
        self.assertTrue(ismail('validemail@domain.sub'))
        self.assertFalse(ismail('@skipusername.sub'))
        self.assertFalse(ismail('noatnoat'))
        self.assertFalse(ismail('skipdomain@'))
        self.assertFalse(ismail('more@then@one.at'))

    # checking cond_b - Name not longer than 128
    def test_cond_b(self):
        self.assertTrue(ismail('w' * 128 + '@domain.sub'))
        self.assertFalse(ismail('w' * 129 + '@domain.sub'))

    # checking cond_c - Minimum domain length 3 symbols. Max domain length 256 symbols
    def test_cond_c(self):
        self.assertTrue(ismail('username@sub'))
        self.assertFalse(ismail('username@su'))
        self.assertTrue(ismail('username@' + 'w' * 256))
        self.assertFalse(ismail('username@' + 'w' * 257))

    # checking cond_d - There are no space in the domain
    def test_cond_d(self):
        self.assertFalse(ismail('username@sub '))
        self.assertFalse(ismail('username@ sub'))
        self.assertFalse(ismail('username@s ub'))

    # checking cond_e - Dot should split domain on two or more none empty parts
    def test_cond_e(self):
        self.assertFalse(ismail('username@domain.'))
        self.assertFalse(ismail('username@.domain'))
        self.assertFalse(ismail('username@dom..ain'))
        self.assertTrue(ismail('username@do.main'))
        self.assertTrue(ismail('username@d.o.m.a.i.n'))

    # checking  cond_f - Domain parts cannot have "-" at the beginning or at the end of the domain part
    def test_cond_f(self):
        self.assertTrue(ismail('username@s-b'))
        self.assertFalse(ismail('username@-ub'))
        self.assertFalse(ismail('username@do-'))
        self.assertFalse(ismail('username@dom.-in'))
        self.assertFalse(ismail('username@dom.ai-'))

    # checking cond_g - Possible symbols for domain a-z 0-9._- only
    def test_cond_g(self):
        self.assertTrue(ismail('username@abz0_59.w-r'))
        self.assertTrue(ismail('username@a--_59.w-r'))
        self.assertFalse(ismail('username@ab!z0_59'))
        self.assertFalse(ismail('username@ab$z0_59'))

    # checking cond_h - Possible symbols for username a-z0-9"._- only. (!,:) symbols also possible but in special cases
    def test_cond_h(self):
        self.assertTrue(ismail('a-f-z_0-59.w@doma.in'))
        self.assertTrue(ismail('a-f-z_0-59.w@doma.in'))
        self.assertFalse(ismail('user-#-name@doma.in'))
        self.assertFalse(ismail('user-&-name@doma.in'))
        self.assertFalse(ismail('user-()-name@doma.in'))
        self.assertFalse(ismail('user-?-name@doma.in'))
        self.assertFalse(ismail('user-^-name@doma.in'))

    # checking cond_k - Pair of quotes is possible only
    def test_cond_k(self):
        self.assertTrue(ismail('username""@doma.in'))
        self.assertTrue(ismail('""username@doma.in'))
        self.assertTrue(ismail('"username"@doma.in'))
        self.assertFalse(ismail('"""username@doma.in'))
        self.assertFalse(ismail('u"s"ern"ame@doma.in'))
        self.assertFalse(ismail('"username@doma.in'))

    # checking cond_l - Symbols !,: should go inside the quotes "!,:"
    def test_cond_l(self):
        self.assertTrue(ismail('"!,:"username@doma.in'))
        self.assertTrue(ismail('"username!,:"@doma.in'))
        self.assertFalse(ismail(':"username"@doma.in'))
        self.assertFalse(ismail('"user"!"name"@doma.in'))
        self.assertFalse(ismail('"username",@doma.in'))

    # checking cond_m - Two dot in the row unacceptable for the username ".."
    def test_cond_m(self):
        self.assertFalse(ismail('..username@doma.in'))
        self.assertFalse(ismail('username..@doma.in'))
        self.assertFalse(ismail('user..name@doma.in'))


if __name__ == '__main__':
    unittest.main()