def calculate_discount(membership_type, duration):
    if duration < 0:
        return "Input không hợp lệ"
    if membership_type == "New":
        if duration < 3:
            return 10
        elif duration >= 3 and duration <= 6:
            return 15
        elif duration >= 6 and duration < 12:
            return 20
        elif duration >= 12:
            return 25
    elif membership_type == "Old":
        if duration < 3:
            return 15
        elif duration >= 3 and duration <= 6:
            return 20
        elif duration >= 6 and duration < 12:
            return 25
        elif duration >= 12:
            return 30
    elif membership_type == "Loyal":
        if duration < 3:
            return 15
        elif duration >= 3 and duration <= 6:
            return 20
        elif duration >= 6 and duration < 12:
            return 25
        elif duration >= 12:
            return 40

# Các testcase đã cho
test_cases = [
    ["New", -5],
    ["Old", -10],
    ["Loyal", -219999999],
    ["Loyal", 1],
    ["Loyal", 3],
    ["Loyal", 6],
    ["Loyal", 12],
    ["Old", 2],
    ["Old", 4],
    ["Old", 7],
    ["Old", 13],
    ["New", 2],
    ["New", 5],
    ["New", 8],
    ["New", 120]
]

# Hàm kiểm thử
def run_tests():
    for test_case in test_cases:
        membership_type, duration = test_case
        discount_rate = calculate_discount(membership_type, duration)
        if discount_rate == "Input không hợp lệ":
            print(f"Loại hội là {membership_type}, Thời hình {duration} tháng, Không tìm thấy ưu đãi do input không hợp lệ.")
        else:
            print(f"Loại hội viên {membership_type}, Thời hạn {duration} tháng, Mức ưu đãi: {discount_rate}")

# Chạy kiểm thử
run_tests()
