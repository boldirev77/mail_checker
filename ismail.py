"""
    File name:
    Author: Aleksander Boldyrev
    Python Version: 3.3
"""

import re


def ismail(email):
    name = (email.split('@')[0])
    domain = email.split('@')[-1]


    # cond_a - '@' should be present in the mail only once
    if not len(email.split('@')) == 2:
        return False
    else:

        # cond_b - Name not longer than 128
        if not (0 < len(name) <= 128):
            return False
        else:

            # cond_c - Minimum domain length 3 symbols. Max domain length 256 symbols
            if not (3 <= len(domain) <= 256):
                return False
            else:

                # cond_d - There are no space in the domain
                if (' ' in domain):
                    return False
                else:

                    # cond_e - Dot should split domain on two or more none empty parts

                    if '.' in domain and 0 in [len(prt) for prt in domain.split(".")]:
                        return False
                    else:

                        # cond_f - Domain parts cannot have "-" at the beginning or at the end of the domain part
                        if True in [True if re.search(r'^[-]|[-]$', prt) else False for prt in domain.split(".")]:
                            return False
                        else:

                            # cond_g - Possible symbols for domain a-z 0-9._- only
                            if False in [True if re.search(r'^[a-z0-9._-]$', ch) else False for ch in domain]:
                                return False
                            else:

                                # cond_h - Possible symbols for username a-z0-9"._-!,: only
                                if False in [True if re.search(r'^[A-Za-z0-9"._!,:-]$', ch) else False for ch in name]:
                                    return False
                                else:

                                    # cond_k - Pair of quotes is possible only
                                    if not len(name.split('"')) % 2 != 0:
                                        return False
                                    else:

                                        # cond_l - Symbols !,: should go inside the quotes "!,:"
                                        sub_name = (''.join(name.split("\"")[::2]))
                                        if not (not bool(re.search(r'[!,:]',  sub_name))):
                                            return False
                                        else:

                                            # cond_m - Two dot in the row unacceptable for the username ".."
                                            return '..' not in name


   # if False in check_array:
    #    return False
    #else: return True
