"""Module containing functions for calculating similarity of two texts.
"""
import re
from collections import defaultdict

re_wd = re.compile(r"[\w']+")  # search pattern: words preserving single quotes


def term_freq(text):
    """Calculate term frequencies of a text.

    Parameters
    ----------
    text : str
        Text to be analyzed.

    Returns
    -------
        dict
    """
    special_w = {"she's": "she is", "he's": "he is", "it's": "it is", "there's": "there is"}
    special_w2 = {"'ll": " will", "'m": " am", "'re": " are", "'ve": " have", "can't": "cannot", "n't": " not"}
    special_w3 = {"'s": "", "'d": ""}  # 'd removed for simplicity b/c parsing is context-based

    freq_vector = defaultdict(int)
    gen = (w for w in re.findall(re_wd, text.lower()))
    while True:
        try:
            w = next(gen)

            w = w.strip("'")  # remove single quotes around a word

            # assuming there can only be one apostrophe in a word
            if w in special_w:
                for wd in special_w[w].split():
                    freq_vector[wd] += 1

            else:
                l2 = [s for s in special_w2 if s in w]
                l3 = [s for s in special_w3 if s in w]

                if l2:
                    w = w.replace(l2[0], special_w2[l2[0]])
                    for wd2 in w.split():
                        freq_vector[wd2] += 1
                    continue

                if l3:
                    w = w.replace(l3[0], "")

                freq_vector[w] += 1

        except StopIteration:
            break

    return freq_vector


def dict_extend(d1, d2):
    """Add keys missing in target dict, but present in source dict to target dict with value=0.

    Parameters
    ----------
    d1 : dict
        Target dictionary to be extended.
    d2 : dict
        Source dictionary.

    Returns
    -------
        dict
    """
    d2_upd = {k: 0 for k in d2}
    d_ext = dict(d2_upd, **d1)

    return d_ext


def term_freq_normalize(d):
    """Normalize the term frequencies with the respective magnitude or L2 norm.
    L2 norm = sqrt(sum(square of each frequency)).

    Parameters
    ----------
    d : dict
        Dictionary with term frequencies.

    Returns
    -------
        dict
    """
    l2_norm = sum((v ** 2 for v in d.values())) ** 0.5
    d_norm = {k: v/l2_norm for k, v in d.items()}

    return d_norm


def cosine_similarity(text1, text2):
    """Calculate cosine similarity of 2 texts.
    Cosine similarity is a dot product of 2 normalized vectors of term frequencies.

    Parameters
    ----------
    text1 : str
        First text.
    text2 : str
        Second text.

    Returns
    -------
        float
    """
    if not (text1 and text2):
        return -1

    d1 = term_freq(text1)
    d2 = term_freq(text2)

    d1_norm = term_freq_normalize(dict_extend(d1, d2))
    d2_norm = term_freq_normalize(dict_extend(d2, d1))

    res = 0
    for k in d1_norm:
        res += d1_norm[k]*d2_norm[k]

    return res


if __name__ == '__main__':
    t1 = "The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. " \
         "If you have any participating brands on your receipt, you'll get points based on the cost of the products. " \
         "You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you " \
         "shop and we'll find the savings for you."
    t2 = "The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. " \
         "If you have any eligible brands on your receipt, you will get points based on the total cost of the " \
         "products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt " \
         "after you check out and we will find the savings for you."
    t3 = "We are always looking for opportunities for you to earn more points, which is why we also give you " \
         "a selection of Special Offers. These Special Offers are opportunities to earn bonus points on top " \
         "of the regular points you earn every time you purchase a participating brand. No need to pre-select " \
         "these offers, we'll give you the points whether or not you knew about the offer. We just think it is " \
         "easier that way."
    t4 = 'Text without "matching" words.'

    print(round(cosine_similarity(t1, t1), 4))
    print(round(cosine_similarity(t1, t2), 4))
    print(round(cosine_similarity(t1, t3), 4))
    print(round(cosine_similarity(t1, t4), 4))
