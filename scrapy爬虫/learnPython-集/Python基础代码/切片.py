str = [1, 4, 5, 6, 7, 9, 11, 14, 16]
print(str[-1:])  # 截取最后一个元素
print(str[0:3])  # 截取第一位到第三位的字符
print(str[:])  # 截取字符串的全部字符
print(str[6:])  # 截取第七个字符到结尾
print(str[:-3])  # 截取从头开始到倒数第三个字符之前
print(str[2])  # 截取第三个字符
print(str[::-1])  # 创造一个与原字符串顺序相反的字符串
print(str[-3:-1])  # 截取倒数第三位与倒数第一位之前的字符
print(str[-3:])  # 截取倒数第三位到结尾
print(str[:-5:-3])  # 逆序截取后个数，每3个取一个，而且取是逆向取值
print(str[:10:2])  # 前10个数，每两个取一个
