def add_strings(num1, num2):
    """Adds two  numbers represented as strings."""
    max_len = max(len(num1), len(num2))  # the max length of the two numbers
    num1 = num1.zfill(max_len)  # Pad with zeros
    num2 =  num2.zfill(max_len) # Pad with zeros

    carry = 0  # Carry starts as 0
    result = [] #store the sum digits
    for i in range(max_len - 1, -1, -1):
        digit_sum = int(num1[i]) + int(num2[i]) + carry
        result.append(str(digit_sum % 10))
        carry = digit_sum // 10

    if carry:
        result.append(str(carry))

    return ''.join(result[::-1])  # Reverse and join


def subtract_strings(num1, num2):
    """Subtracts two large numbers represented as strings (num1 - num2)."""
    max_len = max(len(num1), len(num2))
    num1, num2 = num1.zfill(max_len), num2.zfill(max_len)  # Pad with zeros

    result = []
    borrow = 0
    for i in range(max_len - 1, -1, -1):
        diff = int(num1[i]) - int(num2[i]) - borrow
        if diff < 0:
            diff += 10
            borrow = 1
        else:
            borrow = 0
        result.append(str(diff))

    return ''.join(result[::-1]).lstrip('0') or '0'  # Remove leading zeros


def karatsuba(num1, num2):
    """Multiplies two  numbers using the Karatsuba algorithm."""

    if len(num1) == 1 or len(num2) == 1:
        return str(int(num1) * int(num2))

    max_len = max(len(num1), len(num2))
    half = max_len // 2

    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)

    # Split numbers
    a, b = num1[:-half], num1[-half:]
    c, d = num2[:-half], num2[-half:]

    # Recursive steps
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    sum_ab = add_strings(a, b)
    sum_cd = add_strings(c, d)
    ad_bc = subtract_strings(karatsuba(sum_ab, sum_cd), add_strings(ac, bd))

    # Compute final result
    ac_shifted = ac + '0' * (2 * half)  # Multiply by 10^(2*half)
    ad_bc_shifted = ad_bc + '0' * half  # Multiply by 10^(half)

    result = add_strings(add_strings(ac_shifted, ad_bc_shifted), bd)
    return result.lstrip('0') or '0'  # Remove leading zeros


# Test:
num1 = "3141592653589793238462643383279502884197169399375105820974944592"
num2 = "2718281828459045235360287471352662497757247093699959574966967627"
print("product is:", karatsuba(num1, num2))












