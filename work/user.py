from tkinter import *
from tkinter import ttk
from Dao.dao import conn


# 使用cursor()方法获取操作游标
cursor = conn.cursor()

# SQL 查询语句
sql = "SELECT * FROM user"
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        # 打印结果
        # print("fname=%s,lname=%s,age=%s" % \
        #       (fname, lname, age))
except:
    print("Error: 查询数据失败")


root = Tk()
root.title('用户信息')
root.geometry('500x250+380+150')
tree = ttk.Treeview(root, show="headings")  # 表格第一列不显示
tree.grid(row=5, columnspan=4)
tree["columns"] = ("#1", "#2", "#3", "#4", "#5")
tree.column("#1", width=100, anchor='center')
tree.column("#2", width=100, anchor='center')
tree.column("#3", width=100, anchor='center')
tree.column("#4", width=100, anchor='center')
tree.column("#5", width=100, anchor='center')
tree.heading("#1", text="用户id")
tree.heading("#2", text="用户名")
tree.heading("#3", text="密码")
tree.heading("#4", text="用户住址")
tree.heading("#5", text="联系方式")

for row in results:
    tree.insert("", 0, text="", values=row)


def getItem():
    print(tree.selection())
    print(tree.item(tree.selection())['row'])


root.mainloop()
