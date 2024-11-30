def get_password(n):
    if n < 3 or n > 20:
        raise ValueError("n должно быть в диапазоне от 3 до 20")

    password = ""
    used_pairs = set()

    for i in range(1, 21):
        for j in range(i + 1, 21):
            pair_sum = i + j
            if n % pair_sum == 0:
                pair_str1 = f"{i}{j}"
                pair_str2 = f"{j}{i}"

                if pair_str1 not in used_pairs:
                    password += pair_str1
                    used_pairs.add(pair_str1)

    return password

for n in range(3, 21):
    print(f"{n} - {get_password(n)}")
