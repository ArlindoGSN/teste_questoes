
def is_fibonacci(n):
    if n < 0:
        return False
    def fibonacci(max_value):
        fibs = [0, 1]
        while True:
            next_fib = fibs[-1] + fibs[-2]
            if next_fib > max_value:
                break
            fibs.append(next_fib)
        return fibs
    fib_numbers = fibonacci(n)
    return n in fib_numbers

try:
    num = int(input(" Digite um número inteiro: "))
    if is_fibonacci(num):
        print(f"O número {num} pertence a sequência de Fibonacci.")
    else:
        print(f"O número {num} não pertence a sequência de Fibonacci.")
except ValueError:
    print("O valor digitado deve ser um número inteiro.")