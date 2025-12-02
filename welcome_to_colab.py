b1

import math
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

# Kiểm tra điều kiện của a
if a == 0:
    print("a = 0, phương trình trở thành phương trình bậc nhất hoặc không hợp lệ.")
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
    else:
        # Giải phương trình bậc nhất bx + c = 0
        x = -c / b
        print("Phương trình bậc nhất có nghiệm x =", x)

else:
    # Giải phương trình bậc hai
    delta = b**2 - 4*a*c
    print("Giá trị delta =", delta)

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("Phương trình có hai nghiệm phân biệt:")
        print("x1 =", x1)
        print("x2 =", x2)

    elif delta == 0:
        x = -b / (2*a)
        print("Phương trình có nghiệm kép x =", x)

    else:
        print("Phương trình vô nghiệm trong tập số thực.")


b2
# Nhập một số nguyên dương n
n = int(input("Nhập một số nguyên dương n: "))

# Kiểm tra điều kiện n phải >= 0
if n < 0:
    print("Vui lòng nhập một số nguyên dương!")
else:
    tong = 0

    # Dùng vòng lặp for để tính tổng từ 0 đến n
    for i in range(0, n + 1):
        tong += i



    b3
    # Hiển thị kết quả
    print("Tổng các số từ 0 đến", n, "là:", tong)

# Nhập một số nguyên dương n
n = int(input("Nhập một số nguyên dương n: "))

# Kiểm tra n hợp lệ
if n <= 0:
    print("Vui lòng nhập một số nguyên dương!")
else:
    tong = 0      # biến lưu tổng
    i = 0         # bắt đầu từ số chẵn đầu tiên

    # Lặp while để cộng các số chẵn nhỏ hơn n
    while i < n:
        tong += i
        i += 2    # tăng thêm 2 để luôn đi đến số chẵn tiếp theo

    # In kết quả
    print("Tổng các số chẵn nhỏ hơn", n, "là:", tong)
