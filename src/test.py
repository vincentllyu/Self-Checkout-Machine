import sqlite3

conn = sqlite3.connect('itemsDB/itemLibrary.db')
c = conn.cursor()


# c.execute("INSERT INTO products(barcode, name, price, weigh) VALUES(?, ?, ?, ?)", ("123456", "apple", 5.12, 1))
# c.execute("INSERT INTO products(barcode, name, price, weigh) VALUES(?, ?, ?, ?)", ("0644824914893", "RPI", 34.99, 0))
# c.execute("INSERT INTO products(barcode, name, price, weigh) VALUES(?, ?, ?, ?)", ("0073852291797", "hand saniti", 4.99, 1))
# c.execute("INSERT INTO products(barcode, name, price, weigh) VALUES(?, ?, ?, ?)", ("0753727026128", "saniti(large)", 9.99, 0))
# c.execute("INSERT INTO products(barcode, name, price, weigh) VALUES(?, ?, ?, ?)", ("0639277832672", "typeC cable", 8.49, 0))
# c.execute("INSERT INTO products(barcode, name, price, weigh) VALUES(?, ?, ?, ?)", ("X00134DGFJ", "pyCAM", 14.99, 0))
# c.execute("INSERT INTO products(barcode, name, price, weigh) VALUES(?, ?, ?, ?)", ("0073852096521", "Purell", 1, 1))
# # 
# conn.commit()
barcode = "0073852096521"
row = c.execute('SELECT * FROM products WHERE barcode = :bc', {'bc':barcode}).fetchall()
print(row)
if not row:
    barcode,item_name,item_price,sold_by_gram = "", "", 0, 0
else:
    barcode,item_name,item_price,sold_by_gram = row[0]
# barcode,item_name,item_price,sold_by_gram = row
print(barcode,item_name,item_price,sold_by_gram)
# for row in c.execute('SELECT * FROM items'):
#     #print(row)
#     barcode,item_name,item_price,sold_by_gram = row
    
    
conn.close()

#0644824914893  RPI
#0073852291797 PURELL hand saniti
#0753727026128 saniti(large)
#0639277832672 typeC cable
#X00134DGFJ py camera