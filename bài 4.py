def fibonacci_quy_hoach_dong(n):
    fib = [0] * (n + 1)
    fib[0] = 0
    if n > 0:
        fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]
n = int(input("Nhập số n (n phải là số nguyên không âm): "))
if n < 0:
    print("Vui lòng nhập số nguyên không âm.")
else:
    print(f"Số Fibonacci thứ {n} là: {fibonacci_quy_hoach_dong(n)}")
