import sys
file_name = sys.argv[1]

print(file_name)
title = "{:^9}\t{:>18}\t{:^15}\t{:^15}\t{:^15}\t{:^15}\n".format("Student", "Name", "Midterm", "Final", "Average", "Grade")
lines = "----------" * 10 + "\n"

print(title, lines)


