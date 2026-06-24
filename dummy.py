import cupy as cp


def add_arrays(a, b):
    x = cp.array(a)
    y = cp.array(b)
    return (x + y).tolist()


if __name__ == "__main__":
    result = add_arrays([1, 2, 3], [4, 5, 6])
    print(result)  # [5, 7, 9]
