# 🚀 Hướng Dẫn Chạy Dự Án Pandas I

## 📚 Danh Sách File

Dự án này bao gồm 4 file chính:

| File | Mô Tả | Mục Đích |
|------|--------|---------|
| `pandas_project.py` | Ví dụ toàn diện | Học tập - chứa tất cả ví dụ chi tiết |
| `pandas_exercises.py` | Bài tập trắc nghiệm | Thực hành - giải quyết các bài tập |
| `pandas_solutions.py` | Giải pháp tham khảo | Kiểm tra - so sánh kết quả của bạn |
| `README_PANDAS.md` | Tài liệu đầy đủ | Tham khảo - hướng dẫn chi tiết |

## 🎯 Quy Trình Học Tập Được Khuyến Nghị

### Bước 1: Học Lý Thuyết (10-15 phút)
```bash
# Chạy ví dụ toàn diện để hiểu các khái niệm
python3 pandas_env/bin/python pandas_project.py
```

**Điều bạn sẽ học:**
- Cách tạo DataFrame từ dict
- Sử dụng iloc, loc, at, iat
- Làm sạch dữ liệu (rename, NaN, dtype, categorical)
- Sử dụng groupby với agg và transform

### Bước 2: Thực Hành (30-45 phút)
```bash
# Mở file bài tập và bắt đầu giải
python3 pandas_env/bin/python pandas_exercises.py
```

**Hướng dẫn giải quyết:**
1. Đọc kỹ yêu cầu của bài
2. Viết code vào phần `# Viết code ở đây`
3. Chạy file để kiểm tra kết quả
4. So sánh với giải pháp

### Bước 3: So Sánh Kết Quả (10-15 phút)
```bash
# Xem giải pháp tham khảo
python3 pandas_env/bin/python pandas_solutions.py
```

**Điều cần làm:**
1. So sánh code của bạn với code giải pháp
2. Hiểu tại sao giải pháp của bạn đúng/sai
3. Học các cách viết code tốt hơn

## 💻 Các Lệnh Chạy Thực Tế

### Option 1: Sử dụng Virtual Environment (Được khuyên dùng)

```bash
# Di chuyển vào thư mục dự án
cd /home/phucmouse135/Documents/leetcode

# Chạy project chính
./pandas_env/bin/python pandas_project.py

# Chạy bài tập
./pandas_env/bin/python pandas_exercises.py

# Chạy giải pháp
./pandas_env/bin/python pandas_solutions.py
```

### Option 2: Sử dụng Lệnh Tắt

```bash
# Alias giúp dễ dàng hơn
alias pandas_python='/home/phucmouse135/Documents/leetcode/pandas_env/bin/python'

# Sau đó chạy
cd /home/phucmouse135/Documents/leetcode
pandas_python pandas_project.py
pandas_python pandas_exercises.py
pandas_python pandas_solutions.py
```

### Option 3: Tạo Shell Script

Tạo file `run.sh`:
```bash
#!/bin/bash
cd /home/phucmouse135/Documents/leetcode
./pandas_env/bin/python "$@"
```

Sau đó:
```bash
chmod +x run.sh
./run.sh pandas_project.py
./run.sh pandas_exercises.py
```

## 📋 Nội Dung Từng File Chi Tiết

### pandas_project.py (Main Project)

**Phần 1: Tạo Dữ Liệu** (5 min)
- Dữ liệu mô phỏng bán hàng
- 120 rows × 7 columns
- Chứa NaN để thực hành xử lý

**Phần 2: DataFrame Internals** (5 min)
- Hiểu DataFrame là dict của Series
- Truy cập columns, index
- Kiểm tra dtype

**Phần 3: Indexing** (10 min)
- `iloc`: truy cập theo vị trí
- `loc`: truy cập theo tên
- `at/iat`: truy cập 1 phần tử nhanh
- Boolean indexing

**Phần 4: Data Cleaning** (15 min)
- Rename cột
- Handle NaN
- Convert dtype
- Sử dụng categorical

**Phần 5: GroupBy** (15 min)
- agg vs transform
- Các hàm tổng hợp
- Combine agg

**Phần 6-7: Thống kê & Pivot** (10 min)
- Phân tích dữ liệu
- Tạo pivot table

### pandas_exercises.py (Practice)

**7 Bài Tập Chính:**

1. **Indexing** (4 sub-bài)
   - iloc, loc, at/iat, boolean indexing

2. **DataFrame Internals** (3 sub-bài)
   - Truy cập columns, Series, tạo Series mới

3. **Data Cleaning** (4 sub-bài)
   - Rename, NaN, dtype conversion, categorical

4. **GroupBy - agg** (4 sub-bài)
   - agg cơ bản, nhiều hàm, nhiều cột, custom function

5. **GroupBy - transform** (4 sub-bài)
   - transform cơ bản, %, rank, z-score

6. **agg vs transform** (2 sub-bài)
   - So sánh shape, lựa chọn phương pháp

7. **Combined Practice** (3 sub-bài)
   - Pipeline cleaning, category analysis, age group analysis

**Tổng Cộng: 24 sub-bài tập**

### pandas_solutions.py (Solutions)

Chứa giải pháp đầy đủ cho tất cả 24 bài tập với giải thích chi tiết.

## 🧠 Tips & Tricks

### Tip 1: Hiểu sâu hơn về agg vs transform

```python
# agg: giảm dữ liệu
df.groupby('store')['qty'].agg('sum')
# Result: Store A → 276, Store B → 243, ...

# transform: giữ dữ liệu
df.groupby('store')['qty'].transform('sum')
# Result: 120 rows, mỗi hàng là tổng của store tương ứng
```

### Tip 2: Các cách viết loc/iloc

```python
# Các cách tương đương
df.loc[df['store'] == 'A']
df[df['store'] == 'A']

# Điều kiện phức tạp
df.loc[(df['qty'] > 10) & (df['rating'] >= 4)]

# Sử dụng isin
df.loc[df['store'].isin(['A', 'B'])]
```

### Tip 3: Kiểm tra dtype trước khi làm việc

```python
# Luôn check trước
df.info()
df.dtypes

# Đặc biệt với categorical
df['category'].cat.categories
```

### Tip 4: Memory optimization

```python
# Trước: 1092 bytes
df['store'].memory_usage()

# Sau: 284 bytes (75% tiết kiệm!)
df['store'] = df['store'].astype('category')
df['store'].memory_usage()
```

## 🔍 Debugging Tips

### Vấn Đề 1: SettingWithCopyWarning

```python
# ❌ Sai
filtered = df[df['store'] == 'A']
filtered['new_col'] = ...  # Warning!

# ✅ Đúng
filtered = df[df['store'] == 'A'].copy()
filtered['new_col'] = ...
```

### Vấn Đề 2: NaN sau groupby

```python
# Có thể có NaN nếu group rỗng
result = df.groupby('category')['qty'].mean()
# Dùng fillna để xử lý
result.fillna(0)
```

### Vấn Đề 3: Index reset

```python
# Sau groupby, index có thể bị thay đổi
result = df.groupby('store').agg(...)
# Reset index để lấy lại default
result.reset_index()
```

## 📊 Expected Output Samples

### Từ pandas_project.py:

```
Shape: (120, 7)

Type của df['store_name']: <class 'pandas.Series'>

iloc[0, 0]:
2024-01-01 00:00:00

Tổng số lượng bán theo store:
store
Store A    276
Store B    243
Store C    283
Store D    286
```

### Từ pandas_exercises.py:

```
5 hàng đầu, 3 cột đầu:
   date store_name product_category
0 2024-01-01    Store A             Food
1 2024-01-02    Store B            Books
2 2024-01-03    Store C      Electronics

... (24 bài tập khác)
```

## 🎓 Bài Tập Thêm (Nâng Cao)

Nếu bạn muốn thử thêm:

1. **Thêm dữ liệu từ CSV**
   - Tạo file CSV với dữ liệu thực
   - Đọc bằng `pd.read_csv()`

2. **Visualization**
   - Dùng matplotlib hoặc seaborn
   - Vẽ biểu đồ từ groupby results

3. **Time Series Analysis**
   - Tổng hợp dữ liệu theo ngày
   - Tính moving average

4. **Statistical Testing**
   - So sánh giữa các store
   - Kiểm định giả thuyết

## 📞 Cần Giúp?

### Nếu gặp lỗi:

1. Kiểm tra lỗi syntax
   ```bash
   python3 -m py_compile pandas_project.py
   ```

2. Kiểm tra import
   ```bash
   ./pandas_env/bin/python -c "import pandas; print(pandas.__version__)"
   ```

3. Xem traceback đầy đủ
   - Chạy lại file và đọc error message

### Tài liệu tham khảo:

- [Pandas Official Docs](https://pandas.pydata.org/)
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- [Stack Overflow - pandas tag](https://stackoverflow.com/questions/tagged/pandas)

## ✅ Checklist Hoàn Thành

- [ ] Chạy được pandas_project.py
- [ ] Hiểu được agg vs transform
- [ ] Hoàn thành 70% bài tập
- [ ] Hiểu được indexing (loc/iloc/at/iat)
- [ ] Biết cách data cleaning
- [ ] Học được cách tối ưu memory (categorical)

---

**Happy Learning! 🎉**

Hãy bắt đầu với `pandas_project.py` và cố gắng giải quyết tất cả bài tập trong `pandas_exercises.py`!
