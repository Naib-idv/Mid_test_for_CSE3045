def tinh_giai_thua(n):
    if n == 0 or n == 1:
        return 1
    giai_thua = 1
    for i in range(2, n + 1):
        giai_thua *= i
    return giai_thua
n = int(input("Hãy nhập vào một số nguyên dương: "))
if n < 0:
    print("Vui lòng nhập một số nguyên dương.")
else:
    print(f"{n}! = {tinh_giai_thua(n)}")
