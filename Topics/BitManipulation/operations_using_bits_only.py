class Operations:
    def add(x, y):
        abs_x = abs(x)
        abs_y = abs(y)

        if abs_x < abs_y:
            return Operations.add(y, x)

        sign = 1 if x > 0 else -1
        if (x > 0 and y > 0) or (x < 0 and y < 0):
            while abs_y > 0:
                carry = (abs_x & abs_y) << 1
                abs_x = abs_x ^ abs_y
                abs_y = carry
        else:
            while abs_y > 0:
                carry = (~abs_x & abs_y) << 1
                abs_x = abs_x ^ abs_y
                abs_y = carry

        if sign == -1:
            abs_x = -abs_x

        return abs_x

    def minus(x, y):
        return Operations.add(x, -y)

    def multiply(x, y):
        abs_x = abs(x)
        abs_y = abs(y)
        if abs_x < abs_y:
            return Operations.multiply(y, x)

        sign = 1
        if (x > 0 > y) or (x < 0 < y):
            sign = -1

        result = 0
        while abs_y > 0:
            if abs_y & 1:
                result = Operations.add(result, abs_x)

            abs_x = abs_x << 1
            abs_y = abs_y >> 1

        if sign == -1:
            result = -result

        return result

    def divide(x, y):
        if y == 0:
            raise Exception("Can not divide by zero")

        abs_x = abs(x)
        abs_y = abs(y)
        sign = 1
        if Operations.multiply(x, y) < 0:
            sign = -1

        if abs_x < abs_y:
            return 0

        quotient = 1
        original_abs_y = abs(y)
        while (abs_y << 1) <= abs_x:
            abs_y = abs_y << 1
            quotient = quotient << 1

        quotient += Operations.divide(abs_x - abs_y, original_abs_y)

        if sign == -1:
            quotient = -quotient

        return quotient

    def modulus(x, y):
        quotient = Operations.divide(x, y)
        modulus = Operations.minus(x, Operations.multiply(quotient, y))
        if modulus < 0:
            modulus += y

        return modulus

if __name__ == '__main__':
    print(-152 % -10)