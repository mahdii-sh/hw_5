import time


cache = {}


def factorial_with_cache(n):
    if n in cache:
        print(f"Getting {n} from cache")
        return cache[n]

    print(f"Calculating factorial of {n}...")
    time.sleep(1)

    if n == 0 or n == 1:
        result = 1
    else:
        result = n * factorial_with_cache(n - 1)

    cache[n] = result
    return result


def factorial_without_cache(n):
    print(f"Calculating factorial of {n} (no cache)...")
    time.sleep(1)
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_without_cache(n - 1)


start = time.time()
print("No cache")
print("Result:", factorial_without_cache(8))
print("Time:", round(time.time() - start, 2), "seconds\n")

start = time.time()
print("With cache (first time)")
print("Result:", factorial_with_cache(8))
print("Time:", round(time.time() - start, 2), "seconds\n")

start = time.time()
print("With cache (second time)")
print("Result:", factorial_with_cache(8))
print("Time:", round(time.time() - start, 2), "seconds")
