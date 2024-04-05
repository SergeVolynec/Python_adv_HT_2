from fractions import Fraction

a = input('Введите дробь 1 через "/": ')
b = input('Введите дробь 2 через "/": ')

num_a = int(a.split("/")[0])
num_b = int(b.split("/")[0])
den_a = int(a.split("/")[1])
den_b = int(b.split("/")[1])

num_sum_ab = num_a * den_b + num_b * den_a
den_sum_ab = den_a * den_b
sum_ab = str(num_sum_ab) + "/" + str(den_sum_ab)
sum_fract = str(Fraction(num_a, den_a) + Fraction(num_b, den_b))

num_mult_ab = num_a * num_b
den_mult_ab = den_a * den_b
mult_ab = str(num_mult_ab) + "/" + str(den_mult_ab)
mult_fract = str(Fraction(num_a, den_a) * Fraction(num_b, den_b))

print(sum_ab, sum_fract)
print(mult_ab, mult_fract)
