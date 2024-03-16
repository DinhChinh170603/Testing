def classify_student(avg):
    if (avg >= 8.0 and avg <= 10.0):
        return "Giỏi"
    elif (avg >= 6.5 and avg < 8.0):
        return "Khá"
    elif (avg >= 5.0 and avg < 6.5):
        return "Trung bình"
    elif (avg >= 0.0 and avg < 5.0):
        return "Yếu"
    else:
        return "Input không hợp lệ"

# Bảng quyết định
test_cases = [
    (10.0, "Giỏi"),
    (12.0, "Input không hợp lệ"),
    (7.5, "Khá"),
    (-1.0, "Input không hợp lệ"),
    (5.5, "Trung bình"),
    (4.0, "Yếu"),
    (8.5, "Giỏi"),
    (6.0, "Trung bình")
]

for test_case in test_cases:
    avg, expected_result = test_case
    result = classify_student(avg)
    print(f"Với điểm số trung bình là {avg}, loại học viên được kỳ vọng là '{expected_result}'. Kết quả thực tế là '{result}'")
