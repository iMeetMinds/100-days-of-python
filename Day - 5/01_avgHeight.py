student_ht = input("Enter the heights of the students ").split()

for n in range(0, len(student_ht)):
    student_ht[n] = int(student_ht[n])

total_ht = 0
total_std = 0
avg_ht = 0
high_no = student_ht[0]

for std in student_ht:
    total_ht += int(std)
    total_std += 1
    if std > high_no:
        high_no = std

avg_ht = round(total_ht / total_std)
print(f"Average high of group is {avg_ht}")
print(f"Highest height if group is {high_no}")