price_TV=float(input('What is the unit price of a TV?'))
no_tv=int(input('How Many TVs Were Sold?'))
price_DVD=float(input('What is the unit price of a DVD player?'))
no_DVD=int(input('How Many DVD Players Were Sold?'))
price_controller=float(input('What is the unit price of a Game Controller?'))
no_controller=int(input('How Many Game Controllers Were Sold?'))
price_console=float(input('What is the unit price of a Game Console?'))
no_console=int(input('How Many Game Consoles Were Sold?'))
price_cell=float(input('What is the unit price of a Cell Phone?'))
no_cell=int(input('How Many Cell Phones Were Sold?'))
subtotal=no_tv*price_TV+price_DVD*no_DVD \
+price_controller*no_controller+price_console*no_console+no_cell*price_cell
tax=subtotal*0.085
total=subtotal+tax
print("SubTotal:",subtotal)
print("Tax:",tax)
print("Total:",total)
payment_type=int(input('Cash or card?'))
if Card:
 print("Total",total+total%2.5)
else:
  print("Total:",total)
