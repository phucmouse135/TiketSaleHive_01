# Giao diện web cơ bản

Tệp này là một mẫu trang web tĩnh nhỏ, responsive.

Tệp trong dự án:
- `index.html` — trang chính
- `style.css` — style cơ bản
- `script.js` — tương tác nhỏ (nav toggle, form handler)

Mở trang:
- Cách nhanh: mở `index.html` trực tiếp trong trình duyệt.
- Hoặc chạy một server tĩnh (khuyến nghị) để tránh vấn đề CORS khi phát triển:

```bash
# Python 3
cd /path/to/project # ví dụ: /home/phucmouse135/Documents/leetcode
python3 -m http.server 8000
# sau đó mở http://localhost:8000
```

Tuỳ chỉnh:
- Thay `logo` trong `index.html`.
- Chỉnh màu trong `:root` của `style.css`.
- Thêm endpoint backend trong `script.js` nếu muốn gửi form thực sự.

Chỗ nào bạn muốn tôi mở rộng thêm? (ví dụ: navbar cải tiến, animation, hoặc tích hợp backend)