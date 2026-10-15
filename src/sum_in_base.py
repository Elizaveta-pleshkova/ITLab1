from unicodedata import digit


def add_in_base(a: str, b: str, base: int) -> str:
    a_str = a.strip().upper()
    b_str = b.strip().upper()
    valid_chars = list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:base])
    if base == 10:
        r_a = int(a_str)
        r_b = int(b_str)
    else:
        p_a = 1
        r_a = 0
        p_b = 1
        r_b = 0
        for char in reversed(a_str):
            digit_valA = valid_chars.index(char)
            r_a += int(digit_valA) * p_a
            p_a *= base

        for char in reversed(b_str):
            digit_valB = valid_chars.index(char)
            r_b += int(digit_valB) * p_b
            p_b *= base

    summ = r_a + r_b
    summ_in_base = ""
    if summ == 0:
        summ_in_base += "0"
    else:
        while summ > 0:
            summ_in_base += str(summ % base)
            summ //= base
    return summ_in_base[::-1]