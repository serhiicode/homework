txt = "Скільки учнів в классі"
k1, k2, k3 = int(input(f"{txt}, №1\n")), int(input(f"{txt}, №2\n")), int(input(f"{txt}, №3\n"))
vsego_uchenikov = k1 + k2 + k3
vsego_part = vsego_uchenikov // 2 + vsego_uchenikov % 2
print(f'Потрібно купити {vsego_part} парт(и)!')