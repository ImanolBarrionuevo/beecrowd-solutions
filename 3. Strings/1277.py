# Function to determine which students failed attendance
def check_attendance(names, attendance_records):
    exam_denied_students = []
    
    for i in range(len(names)):
        total_classes = 0
        present_count = 0

        for status in attendance_records[i]:
            if status == "P":
                present_count += 1
            if status == "P" or "A":
                total_classes += 1
            if status == "M":
                total_classes -= 1  # Justification or excused absence

        if present_count / total_classes < 0.75:
            exam_denied_students.append(names[i])

    return exam_denied_students

# Main execution block
for j in range(int(input())):
    student_count = int(input())
    names = input().split()
    attendance_records = input().split()

    result = check_attendance(names, attendance_records)
    print(" ".join(result))