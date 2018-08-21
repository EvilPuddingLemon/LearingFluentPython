l = [10, 20, 30, 40, 50, 60]
print(l[:2])  # 在下标2的地方分割
print(l[2:])
s = 'bicycle'
print(s[::3])
print(s[::-1])
print(s[::-2])

invoice = """  
0.....6................................40........52...55........ 
1909  Pimoroni PiBrella                    $17.50    3    $52.50 
1489  6mm Tactile Switch x20                $4.95    2     $9.90 
1510  Panavise Jr. - PV-201                $28.00    1    $28.00 
1601  PiTFT Mini Kit 320x240               $34.95    1    $34.95 
"""
SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
line_items = invoice.split('\n')[2:]
for item in line_items:
    print(item[SKU], item[UNIT_PRICE], item[DESCRIPTION])
#print(line_items)


l2 = list(range(10))
print(l2)
l2[2:5] = [20, 30]
print(l2)
del l2[5:7]
print(l2)
l2[3::2] = [11, 22]
print(l2)
l2[2:5] = [100]
print(l2)
