import math

print(int(-1.2531478432720178e-07))
print('{:.7f}'.format(-1.2531478432720178e-07))
print(-1.2531478432720178e-07)

print(0 == -1.2531478432720178e-07, )

print(math.isclose(0, 1.2531478432720178e-07, rel_tol=1e-7))
print(math.isclose(0, -1.2531478432720178e-07, abs_tol=1e-7))