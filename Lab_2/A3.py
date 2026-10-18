import sys

bytes_given = 1921000
megabytes_given = bytes_given / 1024 / 1024
print(f"Из условия: {megabytes_given:.4f} МБ")

number = 3 ** 9090001
real_bytes = sys.getsizeof(number)
real_megabytes = real_bytes / 1024 / 1024
print(f"В реальности: {real_megabytes:.4f} МБ")
