import pymysql
import xlrd
import xlwt

host = 'localhost'
user = 'root'
password = 'root'
database = 'shopping'


# 增
def insert(sql, a):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()
    cursor.execute(sql, a)
    con.commit()
    cursor.close()
    con.close()


# 删
def delete(sql, a):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()
    cursor.execute(sql, a)
    con.commit()
    cursor.close()
    con.close()


# 改
def update(sql, a):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()
    cursor.execute(sql, a)
    con.commit()
    cursor.close()
    con.close()


# 查
def select(sql, a, model, size):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()
    cursor.execute(sql, a)
    if model == 'all':
        return cursor.fetchall()
    elif model == "one":
        return cursor.fetchone()
    elif model == 'many':
        return cursor.fetchmany(size)
    con.commit()
    cursor.close()
    con.close()


# excel_to_db
# wd = xlrd.open_workbook('12月份衣服销售数据.xlsx', encoding_override=True)
# sheet = wd.sheet_by_index(0)
# row = sheet.nrows
# col = sheet.col
#
# for i in range(1, row):
#     date = sheet.cell_value(i, 0)
#     name = sheet.cell_value(i, 1)
#     price = sheet.cell_value(i, 2)
#     count = sheet.cell_value(i, 3)
#     sales = sheet.cell_value(i, 4)
#     sql = 'insert into clothes values(%s,%s,%s,%s,%s)'
#     b = [date, name, price, count, sales]
#     insert(sql, b)
# db_to_excel
table_name = xlwt.Workbook()
sql = 'select*from  clothes'
a = None
model = 'all'
size = None
b = select(sql, a, model, size)
sheet = table_name.add_sheet('12月')
fields = ['日期', '服装名称', '价格/件', '库存数量', '销售量/每日']  # 获取所有字段名
for col, field in enumerate(fields):
    sheet.write(0, col, field)
row = 1
for i in b:
    print(i)
    for col, field in enumerate(i):
        sheet.write(row, col, field)
    row += 1
table_name.save('12月份衣服销售情况.xls')
