"""
    File name:
    Author: Aleksander Boldyrev
    Python Version: 3.3
"""

import re


def mcheck(email):
    check_array = []
    name = email.split('@')[0]
    domain = email.split('@')[-1]

    # cond_a - '@' should be present in the mail only once
    check_array.append(len(email.split('@')) == 2)

    # cond_b - Name not longer than 128
    check_array.append(0 < len(name) < 128)

    # cond_c - Minimum domain length 3 symbols. Max domain length 256 symbols
    check_array.append(3 <= len(domain) < 256)

    # cond_d - There are no space in the domain
    check_array.append(' ' not in domain)

    # cond_e - Dot should split domain on two parts
    check_array.append(len(domain.split('.', 1)[0]) < len(domain)-1)

    # cond_f - Possible symbols for domain a-z 0-9_- only
    if False in [True if re.search(r'^[a-z0-9._-]$', ch) else False for ch in domain]:
        check_array.append(False)
    else: check_array.append(True)

    # cond_g - Domain parts cannot have "-" at the beginning or at the end of the domain part
    domain_parts = domain.split("."),
    if '-' in ''.join([part[0]+part[-1] for part in domain_parts]):
        check_array.append(False)
    else:
        check_array.append(True)

    # cond_h - Possible symbols for username a-z0-9"._-!,: only
    if False in [True if re.search(r'^[A-Za-z0-9"._!,:-]$', ch) else False for ch in name]:
        check_array.append(False)
    else: check_array.append(True)

    # cond_k - Two dot in the row unexceptable for the username ".."
    check_array.append('..' not in name)

    # cond_l - Pair of quotes is possible only
    check_array.append(len(name.split('"')) % 2 != 0)

    # cond_m - Symbols !,: should go inside the quotes "!,:"
    inside_symbols = '!,:'
    name_substr = (re.sub(r'".*[%s].*"' % inside_symbols, '', name))
    check_array.append(not bool(re.search(r'[%s]' % inside_symbols, name_substr)))

    if False in check_array:
        return False
    else: return True