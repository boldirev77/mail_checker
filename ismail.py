"""
    File name:
    Author: Aleksander Boldyrev
    Python Version: 3.3
"""

import re


def ismail(email):
    check_array = []
    name = email.split('@')[0]
    domain = email.split('@')[-1]

    # cond_a - '@' should be present in the mail only once
    check_array.append(len(email.split('@')) == 2)

    # cond_b - Name not longer than 128
    check_array.append(0 < len(name) <= 128)

    # cond_c - Minimum domain length 3 symbols. Max domain length 256 symbols
    check_array.append(3 <= len(domain) <= 256)

    # cond_d - There are no space in the domain
    check_array.append(' ' not in domain)

    # cond_e - Dot should split domain on two or more none empty parts
    if '.' in domain:
        if 0 in [len(prt) for prt in domain.split(".")]:
            check_array.append(False)
        else:
            check_array.append(True)
    else: check_array.append(True)

    # cond_f - Domain parts cannot have "-" at the beginning or at the end of the domain part
    try:
        if '-' in ''.join([prt[0]+prt[-1] for prt in domain.split(".")]):
            check_array.append(False)
        else: check_array.append(True)
    except IndexError:
        pass

    # cond_g - Possible symbols for domain a-z 0-9._- only
    if False in [True if re.search(r'^[a-z0-9._-]$', ch) else False for ch in domain]:
        check_array.append(False)
    else: check_array.append(True)

    # cond_h - Possible symbols for username a-z0-9"._-!,: only
    if False in [True if re.search(r'^[A-Za-z0-9"._!,:-]$', ch) else False for ch in name]:
        check_array.append(False)
    else: check_array.append(True)

    # cond_k - Pair of quotes is possible only
    check_array.append(len(name.split('"')) % 2 != 0)

    # cond_l - Symbols !,: should go inside the quotes "!,:"
    sub_name = (''.join(name.split("\"")[::2]))
    check_array.append(not bool(re.search(r'[!,:]',  sub_name)))

    # cond_m - Two dot in the row unexceptable for the username ".."
    check_array.append('..' not in name)


    if False in check_array:
        return False
    else: return True

