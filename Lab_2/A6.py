total_seconds = int(input())

total_seconds %= 86400

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print('{}:{:02}:{:02}'.format(hours, minutes, seconds))
