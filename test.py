# year = 2025
# event = 'Referendum'
# print(f'Results of the {year} {event}')

# import math
# print(f'The value of pi is approximately {math.pi:.5f}.')

# table = {'Sjoerd': 412711.85676575, 'Jack': 40981, 'Dcab': 7678}
# for name, phone in table.items():
# print(f'{name:10} ==> {phone:<10}')

# print('We are the {} who say "{}!"'.format('knights', 'Ni'))

# print('{0} and {1} or {2}'.format('spam', 'eggs', 'x'))
# print('{1} and {2} or {0}'.format('spam', 'eggs', 'x'))

# print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))

# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
# print('Jack: {0[Jack]:d};'' Sjoerd: {0[Sjoerd]:d}; ''Dcab: {0[Dcab]:d}'.format(table))

# def scope_test():
#     def do_local():
#         spam = "local spam"

#     def do_nonlocal():
#         nonlocal spam
#         spam = "nonlocal spam"

#     def do_global():
#         global spam
#         spam = "global spam"

#     spam = "test spam"
#     do_local()
#     print("After local assignment:", spam)
#     do_nonlocal()
#     print("After nonlocal assignment:", spam)
#     do_global()
#     print("After global assignment:", spam)


# scope_test()
# print("In global scope:", spam)

# def test():
#     a = int(input("请输入第一个整数的值："))
#     b = int(input("请输入第二个整数的值："))
#     sum1 = a + b
#     sum2 = a - b
#     print(f"第一个整数和第二个整数的和为:{a}+{b}={sum1}")
#     print(f"第一个整数和第二个整数的差为:{a}-{b}={sum2}")


# if __name__ == "__main__":
#     test()

# def factorial():
#     n = int(input("请输入一个自然数："))
#     factorial = 1

#     if n < 0:
#         print("错误：自然数必须 ≥ 0！")
#     elif n == 0:
#         print("0! = 1")
#     else:
#         for i in range(1, n + 1):
#             factorial *= i
#             print(f"{n}! = {factorial}")


# if __name__ == "__main__":
#     factorial()

# sname = 'siray'
# sage = 20
# # print("我的英文名叫%s,年龄%d" % (sname, sage))

# sname = 'siray'
# sage = 20
# print("我的英文名叫{},年龄{}".format(sname, sage))

# sname = 'siray'
# sage = 20
# print(f'我的英文名叫{sname},年龄{sage}')

# a = int(input('请输入第1个数：'))
# b = int(input('请输入第2个数：'))
# c = int(input('请输入第3个数：'))
# d = int(input('请输入第4个数：'))


# def find_max():
#     max = a
#     if b > a:
#         max = b
#     if c > max:
#         max = c
#     if d > max:
#         max = d
#     return max


# if __name__ == "__main__":
#     max = find_max()

# print(f'四个数中最大的为：{max}')


# def lucky_num():
#     num = int(input('请输入一个四位数的数字：'))
#     a = (num // 1000) % 10
#     b = (num // 100) % 10
#     c = (num // 10) % 10
#     d = num % 10
#     if b > a and d == (b + a + c):
#         print(num, "是幸运数字")
#     else:
#         print(num, "不是幸运数字")


# if __name__ == "__main__":
#     lucky_num()

# def count_7():
#     count = 0
#     for i in range(1, 101):
#         if i % 7 == 0 or i % 10 == 7:
#             print(i, end=' ')
#             count = count + 1
#             if count % 5 == 0:
#                 print()


# if __name__ == "__main__":
#     count_7()
