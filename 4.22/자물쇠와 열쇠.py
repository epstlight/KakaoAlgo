def solution(key, lock):
    lock_size = len(lock)
    key_size = len(key)
    new_lock_size = lock_size + key_size * 2 - 2
    for k in range(4):
        for i in range(new_lock_size - key_size + 1):
            for j in range(new_lock_size - key_size + 1):
                if expansion_lock(key, lock, j, i, new_lock_size):
                    return True
        if k < 3 : key = rotate(key)

    return False

def rotate(key):
    size = len(key)
    new_key = [[0] * size for _ in range(size)]

    for i in range(size):
        for j in range(size):
            new_key[j][size - i - 1] = key[i][j]

    return new_key

def expansion_lock(key, lock, start_x, start_y, new_lock_size):
    lock_size = len(lock)
    key_size = len(key)
    new_lock = [[0] * new_lock_size for _ in range(new_lock_size)]
    for i in range(key_size):
        for j in range(key_size):
            new_lock[start_y + i][start_x + j] = key[i][j]

    for i in range(key_size - 1, key_size + lock_size - 1):
        for j in range(key_size - 1, key_size + lock_size - 1):
            new_lock[i][j] += lock[i - key_size + 1][j - key_size + 1]
            if new_lock[i][j] != 1: return False

    return True

