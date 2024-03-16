def is_square(d, r):
    if 0.0 <= d <= 20.0 and 0.0 <= r <= 20.0:
        if d == r:
            return True, "Hình vuông"
        else:
            return False, "Hình chữ nhật"
    else:
        return False, "Đầu vào không hợp lệ"


# Các trường hợp kiểm thử giá trị biên
test_cases = [
    (0.0, 0.0),  
    (20.0, 20.0),
    (0.0, 20.0),
    (20.0, 0.0),
    (0.0, 10.0),  
    (10.0, 0.0),  
    (20.0, 10.0),  
    (10.0, 20.0),  
    (10.0, 10.0)  
]

for test_case in test_cases:
    d, r = test_case
    result, message = is_square(d, r)
    print(f"Với d = {d}, r = {r}: {message}")
