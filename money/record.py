import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
from datetime import datetime



categories = ['Food', 'Transportation', 'Entertainment', 'Others']
expenses = [0, 0, 0, 0]
expense_records = []


# 记录每天的支出
def record_expense(category, amount, date):
    if category in categories:
        index = categories.index(category)
        expenses[index] += amount

        expense_record = {'Category': category, 'Amount': amount, 'Date': date}
        expense_records.append(expense_record)
        print("Expense recorded: {} - ${} - {}".format(category, amount, date))
    else:
        print("Invalid category")


# 可视化支出数据
def visualize_expenses():
    # 隐藏没有开销的类别
    show_labels = [label for index, label in enumerate(categories) if expenses[index] > 0]
    show_expenses = [expense for expense in expenses if expense > 0]

    plt.figure(figsize=(8, 6))
    plt.pie(show_expenses, labels=show_labels, autopct='%1.1f%%')
    plt.title('Daily Expense')
    plt.axis('equal')
    plt.savefig('daily_expenses.png')
    img = plt.imread('daily_expenses.png')
    plt.imshow(img)
    plt.show()


# 保存支出记录到CSV文件
def save_expense_records():
    df = pd.DataFrame(expense_records)
    df.to_csv('expense_records.csv', index=False)


# 加载已有的支出记录
def load_expense_records():
    try:
        df = pd.read_csv('expense_records.csv')
        for index, row in df.iterrows():
            record_expense(row['Category'], row['Amount'], row['Date'])
    except FileNotFoundError:
        print("Expense record not found")


# 按年月日对支出记录进行分组，并返回每天各项类别开销总额的DataFrame
def group_by_date_and_sum(freq):
    df = pd.DataFrame(expense_records)
    df['Amount'] = pd.to_numeric(df['Amount'])
    df['Date'] = pd.to_datetime(df['Date'])
    if freq == 'year':
        grouped = df.groupby(df['Date'].dt.year)
    elif freq == 'month':
        grouped = df.groupby([df['Date'].dt.year, df['Date'].dt.month])
    else:
        grouped = df.groupby([df['Date'].dt.year, df['Date'].dt.month, df['Date'].dt.day])
    summaries = []
    for date, group in grouped:
        summary = {}
        if freq == 'year':
            summary['Date'] = date
        elif freq == 'month':
            year, month = date
            summary['Date'] = datetime(year, month, 1).strftime("%Y-%m")
        else:
            year, month, day = date
            summary['Date'] = datetime(year, month, day).strftime("%Y-%m-%d")
        for category in categories:
            amount_sum = group[group['Category'] == category]['Amount'].sum()
            summary[category] = amount_sum
        summaries.append(summary)
    return pd.DataFrame(summaries)


# GUI应用程序
class ExpenseRecorderApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Daily Expense Recorder")
        self.geometry("400x600")
        self.configure(background='white')

        self.category_label = tk.Label(self, text="Category:", bg='white', fg='black', font=('Arial', 12))
        self.category_label.pack(pady=10)

        self.category_choices = tk.StringVar(self)
        self.category_choices.set(categories[0])

        self.category_menu = tk.OptionMenu(self, self.category_choices, *categories)
        self.category_menu.config(bg='white', fg='black', font=('Arial', 12))
        self.category_menu.pack()

        self.amount_label = tk.Label(self, text="Amount:", bg='white', fg='black', font=('Arial', 12))
        self.amount_label.pack(pady=10)

        self.amount_entry = tk.Entry(self, font=('Arial', 12))
        self.amount_entry.pack()

        self.date_label = tk.Label(self, text="Date(YYYY-MM-DD):", bg='white', fg='black', font=('Arial', 12))
        self.date_label.pack(pady=10)

        self.date_entry = tk.Entry(self, font=('Arial', 12))
        self.date_entry.pack()

        self.record_button = tk.Button(self, text="Record Expense", command=self.record, bg='white', fg='black', font=('Arial', 12))
        self.record_button.pack(pady=20)

        self.visualization_button = tk.Button(self, text="Show Expense Visualization", command=self.visualize, bg='white', fg='black', font=('Arial', 12))
        self.visualization_button.pack(pady=10)

        self.view_records_button = tk.Button(self, text="View Expense Records", command=self.view_records, bg='white', fg='black', font=('Arial', 12))
        self.view_records_button.pack(pady=10)

        self.delete_record_label = tk.Label(self, text="Delete Expense Record:", bg='white', fg='black', font=('Arial', 12))
        self.delete_record_label.pack(pady=10)

        self.delete_date_label = tk.Label(self, text="Date(YYYY-MM-DD):", bg='white', fg='black', font=('Arial', 12))
        self.delete_date_label.pack()

        self.delete_date_entry = tk.Entry(self, font=('Arial', 12))
        self.delete_date_entry.pack()

        self.delete_button = tk.Button(self, text="Delete Record", command=self.delete_record, bg='white', fg='black', font=('Arial', 12))
        self.delete_button.pack(pady=10)

    def record(self):
        category_choice = self.category_choices.get()
        amount = float(self.amount_entry.get())
        date = self.date_entry.get()

        if not date:
            now = datetime.now()
            date = now.strftime("%Y-%m-%d")

        record_expense(category_choice, amount, date)

    def visualize(self):
        visualize_expenses()


    """def view_yearly_expenses(self):
        df = group_by_date_and_sum('year')
        plt.figure(figsize=(8, 6))
        for category in categories:
            plt.plot(df['Date'], df[category], label=category)
        plt.xlabel('Year')
        plt.ylabel('Amount')
        plt.title('Yearly Expenses')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def view_monthly_expenses(self):
        df = group_by_date_and_sum('month')
        plt.figure(figsize=(8, 6))
        for category in categories:
            plt.plot(df['Date'], df[category], label=category)
        plt.xlabel('Month')
        plt.ylabel('Amount')
        plt.title('Monthly Expenses')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def view_daily_expenses(self):
        df = group_by_date_and_sum('day')
        plt.figure(figsize=(8, 6))
        for category in categories:
            plt.plot(df['Date'], df[category], label=category)
        plt.xlabel('Day')
        plt.ylabel('Amount')
        plt.title('Daily Expenses')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
"""
    """
    def visualize_data(self, interval):
        grouped_sums = group_by_date_and_sum(interval)
        categories = list(grouped_sums.columns)[1:]

        # 获取日期列表并按升序排序
        dates = sorted(list(grouped_sums['Date']))

        # 生成x轴标签和位置
        x_labels = [datetime.strptime(date, '%Y-%m-%d').date().strftime('%Y-%m-%d') for date in dates]
        x_pos = range(len(x_labels))

        # 绘制柱状图
        plt.figure(figsize=(10, 6))
        for i, category in enumerate(categories):
            values = []
            for date in dates:
                # 查找该日期下该类别的开销
                row = grouped_sums[grouped_sums['Date'] == date]
                value = row[category].values[0] if not row.empty else 0
                values.append(value)
            plt.bar(x_pos, values, align='center', alpha=0.5, label=category)
            x_pos = [x + 1 for x in x_pos]

        # 设置x轴标签和范围
        plt.xticks(range(len(x_labels)), x_labels, rotation=45)
        plt.xlim([-1, len(x_labels)])

        plt.xlabel('Date')
        plt.ylabel('Expense')
        plt.title('Expense Visualization')
        plt.legend()
        plt.tight_layout()  # 调整布局以使柱状图填充整个画布
        plt.show()"""
    def view_records(self):
        save_expense_records()
        daily_sums = group_by_date_and_sum('day')
        records_window = tk.Toplevel(self)
        records_window.title("Expense Records")

        scrollbar = tk.Scrollbar(records_window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_area = tk.Text(records_window, yscrollcommand=scrollbar.set, bg='white', fg='black', font=('Arial', 12))
        text_area.insert(tk.END, "Daily Expenses:\n\n")

        for index, row in daily_sums.iterrows():
            text_area.insert(tk.END, "{}:\n".format(row['Date']))
            for category in categories:
                text_area.insert(tk.END, "{}: ${}\t".format(category, row[category]))
            text_area.insert(tk.END, "\n\n")

        text_area.pack(side=tk.LEFT, fill=tk.BOTH)

        scrollbar.config(command=text_area.yview)

    def delete_record(self):
        date = self.delete_date_entry.get()
        if not date:
            print("Please enter a valid date")
            return
        df = pd.DataFrame(expense_records)
        df['Date'] = pd.to_datetime(df['Date'])
        df = df[df['Date'] != date]

        # 更新全局变量
        expense_records.clear()
        for index, row in df.iterrows():
            record_expense(row['Category'], row['Amount'], row['Date'])

        save_expense_records()
        print("Expense record deleted")

# 程序入口
if __name__ == '__main__':
    load_expense_records()  # 加载之前保存的支出记录
    app = ExpenseRecorderApp()
    app.mainloop()
    save_expense_records()  # 保存当前的支出记录到CSV文件