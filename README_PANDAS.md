# 📊 Pandas I - DataFrame Internals, Indexing, GroupBy Project

## Giới thiệu
Dự án này cung cấp hướng dẫn toàn diện và thực hành về các khái niệm cơ bản của Pandas:
- DataFrame internals - hiểu cấu trúc bên trong
- Indexing - làm chủ loc, iloc, at, iat
- Data Cleaning - làm sạch và chuẩn hóa dữ liệu
- GroupBy - tổng hợp dữ liệu theo nhóm

## 📁 Cấu trúc Dự án

```
pandas_project.py       # File chính chứa tất cả ví dụ và thực hành
README.md              # Tệp này
```

## 🎯 Nội dung chính

### Phần 1: Tạo Dữ Liệu Mẫu
- Tạo dataset mô phỏng dữ liệu bán hàng của 4 cửa hàng
- 120 hàng dữ liệu với 7 cột
- Bao gồm NaN để thực hành xử lý dữ liệu

### Phần 2: Hiểu DataFrame là Dict của Series
```python
# DataFrame là dict của các Series
df['column_name']  # Trả về Series
df.columns         # Tên tất cả cột
df.index          # Index của tất cả hàng
```

### Phần 3: Indexing - loc, iloc, at, iat

| Phương thức | Loại | Trích xuất | Tốc độ | Dùng khi |
|-----------|------|----------|-------|---------|
| `loc` | Label-based | Nhiều/1 giá trị | Chậm | Cần linh hoạt |
| `iloc` | Position-based | Nhiều/1 giá trị | Chậm | Dùng vị trí số |
| `at` | Label-based | 1 giá trị | Nhanh | Cần 1 giá trị duy nhất |
| `iat` | Position-based | 1 giá trị | Nhanh | Cần 1 giá trị duy nhất |

**Ví dụ:**
```python
df.iloc[0, 0]              # Hàng 0, cột 0
df.loc[0, 'store_name']    # Hàng 0, cột 'store_name'
df.at[5, 'store_name']     # Nhanh: hàng 5, cột 'store_name'
df.iat[5, 2]               # Nhanh: hàng 5, cột thứ 2
df.loc[df['qty'] > 15]     # Điều kiện
```

### Phần 4: Data Cleaning

#### 4.1 Đổi tên cột
```python
df.rename(columns={'old_name': 'new_name'})
```

#### 4.2 Xử lý NaN
```python
df['column'].fillna(value)           # Fill giá trị cụ thể
df['column'].fillna(df['column'].median())  # Fill bằng median
df.dropna()                          # Xóa hàng có NaN
```

#### 4.3 Ép kiểu
```python
df['column'].astype('int32')         # Chuyển sang int32
df['column'].astype('float32')       # Chuyển sang float32
df['column'].astype('int8')          # Tiết kiệm bộ nhớ
```

#### 4.4 Categorical
```python
df['column'] = df['column'].astype('category')  # Chuyển sang category
df['column'].cat.categories                      # Xem categories
```

**Lợi ích của categorical:**
- Tiết kiệm bộ nhớ (đặc biệt với các cột có ít unique values)
- Tăng tốc độ xử lý
- Phù hợp cho các biến có thứ tự hoặc định danh

### Phần 5: GroupBy - agg vs transform

#### 5.1 agg (Aggregation - Tập hợp)
**Dùng khi:** Muốn GIẢM số lượng hàng
**Kết quả:** Ít hàng hơn dữ liệu gốc (thường groupby key)

```python
# Tổng số lượng bán theo store
df.groupby('store')['quantity'].sum()

# Nhiều hàm trên nhiều cột
df.groupby('store')[['quantity', 'price']].agg({
    'quantity': ['sum', 'mean', 'max'],
    'price': ['min', 'max']
})
```

#### 5.2 transform (Transformation - Biến đổi)
**Dùng khi:** Muốn GIỮ số lượng hàng, thêm cột mới
**Kết quả:** Cùng số hàng + cột mới

```python
# Thêm cột trung bình của store
df['store_avg'] = df.groupby('store')['quantity'].transform('mean')

# Thêm cột tỷ phần trăm
df['pct'] = df.groupby('store')['quantity'].transform(lambda x: x / x.sum() * 100)

# Thêm cột rank trong store
df['rank'] = df.groupby('store')['quantity'].transform('rank')
```

#### 5.3 So sánh
- **agg**: 120 rows → 4 rows (1 hàng per store)
- **transform**: 120 rows → 120 rows + cột mới

### Phần 6: Thống kê và Insights
Phân tích dữ liệu với các hàm:
- `describe()` - thống kê cơ bản
- `agg()` - tổng hợp tùy chỉnh
- `pivot_table()` - tạo bảng tóm tắt

### Phần 7: Pivot Table
```python
pivot = df.pivot_table(
    values='quantity',
    index='store',
    columns='category',
    aggfunc='sum',
    fill_value=0
)
```

## 🚀 Cách chạy

```bash
# Chạy file chính
python pandas_project.py

# Hoặc nếu dùng Python 3 cụ thể
python3 pandas_project.py

# Nếu đã cấu hình môi trường
/usr/bin/python pandas_project.py
```

## 📚 Kiến thức Chính

### DataFrame Internals
```python
# DataFrame là dict của Series
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})
# Tương đương với:
{'A': Series([1,2,3]), 'B': Series([4,5,6])}
```

### Indexing Hierarchy
1. **loc/iloc** - Linh hoạt, có thể lấy nhiều giá trị
2. **at/iat** - Nhanh, chỉ lấy 1 giá trị
3. **Boolean indexing** - Lấy theo điều kiện

### Data Cleaning Pipeline
```
Nguyên liệu → Đổi tên cột → Xử lý NaN → Ép kiểu → Categorical → Phân tích
```

### GroupBy Logic
```
Đầu vào → GroupBy key → Nhóm 1, Nhóm 2, ...
                           ↓
                      agg: Tóm tắt → Ít hàng
                      transform: Thêm cột → Cùng hàng
```

## 💡 Mẹo và Best Practices

1. **Luôn check dtype trước khi làm việc**
   ```python
   df.dtypes
   df.info()
   ```

2. **Sử dụng categorical cho cột với ít unique values**
   ```python
   df['store'] = df['store'].astype('category')
   ```

3. **Dùng at/iat thay vì loc/iloc khi chỉ cần 1 giá trị**
   ```python
   # Nhanh
   value = df.at[0, 'column']
   # Chậm
   value = df.loc[0, 'column']
   ```

4. **Chọn agg hay transform theo mục đích**
   - Muốn tóm tắt? → agg
   - Muốn thêm cột? → transform

5. **Luôn xử lý NaN trước khi tính toán**
   ```python
   df.isnull().sum()  # Kiểm tra
   df.fillna()        # Xử lý
   ```

## 🎓 Bài Tập Thêm

1. **Bài 1**: Tìm store có satisfaction score cao nhất
2. **Bài 2**: Tính tổng doanh thu (quantity * price) theo store
3. **Bài 3**: Tìm sản phẩm (category) bán chạy nhất trong từng store
4. **Bài 4**: Tính z-score cho quantity bán trong từng store
5. **Bài 5**: Tạo pivot table với doanh thu

## 📖 Tài liệu tham khảo

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Indexing and Selecting Data](https://pandas.pydata.org/docs/user_guide/indexing.html)
- [Groupby](https://pandas.pydata.org/docs/user_guide/groupby.html)

---
**Tạo bởi**: Pandas Learning Project  
**Ngày**: 2024  
**Mục đích**: Học tập và thực hành Pandas cơ bản
