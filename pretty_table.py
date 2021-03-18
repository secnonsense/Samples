from prettytable import PrettyTable
table = PrettyTable()

table.field_names = ['Name', 'Age', 'City']
table.add_row(["Alice", 20, "Adelaide"])
table.add_row(["Bob", 20, "Brisbane"])
table.add_row(["Chris", 20, "Cairns"])
table.add_row(["David", 20, "Sydney"])
table.add_row(["Ella", 20, "Melbourne"])

table.sortby = "City"
print(table)
print(table.get_html_string())
