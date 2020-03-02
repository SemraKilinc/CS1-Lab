tax_rate=8.5 
labour_rate=0.35 
def readquestions(): 
  global length_of_room
  length_of_room=int(input("\nLength of the room(feet)? "))
  global width_of_room
  width_of_room=int(input("\nWidth of the room(feet)? "))
  global discount_rate
  discount_rate=float(input("\nDiscount(percent)? "))
  global cost
  cost=float(input("\nCost per square foot(XXX.XX)? "))
def calculate_install_price(): 
  global area
  area=length_of_room*width_of_room
  global carpet_cost
  carpet_cost=area*cost
  global labour_cost
  labour_cost=area*labour_rate
  installed_price=carpet_cost+labour_cost
  return installed_price
def calculate_subtotal(installed_price):
  global discount
  discount=(discount_rate/100)*installed_price
  subtotal = installed_price - discount
  return subtotal
def calculate_total(subtotal): 
  global tax
  tax = tax_rate*subtotal
  total=subtotal+tax
  return total
def calculate_values(): 
  global install_price
  install_price=calculate_install_price()
  global subtotal
  subtotal=calculate_subtotal(install_price)
  global total
  total=calculate_total(subtotal)
def print_measurement():
  print("MEASUREMENT".center(40),"\n") 
  width=10
  print("\nLength".ljust(width)+"\t\t\t"+f"{length_of_room} ft".ljust(width)) 
  print("\nWidth".ljust(width)+"\t\t\t"+f"{width_of_room} ft".ljust(width))
  print("\nArea".ljust(width)+"\t\t\t"+f"{area} square ft".ljust(width))
def print_charges(): 
  width=12
  print("CHARGES".center(40),"\n")
  print("\nDESCRIPTION".ljust(width)+"\tCOST/SQ.FT.".ljust(width)+"\tCHARGE".rjust(6)) 
  print("\nCarpet".ljust(width)+f"\t{cost}\t".ljust(14)+f"$ {carpet_cost:9.2f}".rjust(6)) 
  print("\nLabor".ljust(width)+f"\t{labour_rate}\t".ljust(14)+f"{labour_cost:9.2f}".rjust(6))
  print("\nINSTALLED PRICE".ljust(width)+"\t\t\t"+f"${install_price:9.2f}".rjust(6))
  print("\nDiscount".ljust(width)+f"\t{discount_rate}\t".ljust(14)+f"{discount:9.2f}".rjust(6))
  print("\nSUBTOTAL".ljust(width)+"\t\t\t"+f"${subtotal:9.2f}".rjust(6))
  print("\nTax".ljust(width)+"\t\t\t"+f"{tax:9.2f}".rjust(6))
  print("\nTOTAL".ljust(width)+"\t\t\t"+f"${total:9.2f}".rjust(6))
def print_result():
  print_measurement()
  print_charges()
def main(): 
  readquestions()
  calculate_install_price()
  calculate_values()
  print_result()
main() 