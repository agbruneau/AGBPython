def fibonacci(n):
    """
    Génère une liste contenant les n premiers nombres de Fibonacci.
    :param n: Le nombre de termes de la séquence de Fibonacci à générer.
    :return: Une liste des n premiers nombres de Fibonacci.
    """
    fib_numbers = [0, 1]
    for i in range(2, n):
        next_fib = fib_numbers[-1] + fib_numbers[-2]
        fib_numbers.append(next_fib)
    return fib_numbers[:n]

def main():
    # Modifier cette valeur pour générer plus ou moins de nombres de Fibonacci
    n = 10000  # Par exemple, les 100 premiers nombres de Fibonacci

    # Générer et afficher la liste de Fibonacci
    fib_list = fibonacci(n)
    for i, fib_num in enumerate(fib_list):
        print(f"Fibonacci({i}): {fib_num}")

if __name__ == "__main__":
    main()
