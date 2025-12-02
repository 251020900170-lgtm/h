b2
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






b1
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

    # Hiển thị kết quả
    print("Tổng các số từ 0 đến", n, "là:", tong)
