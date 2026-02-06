# micro_level_practice_2.py
# This file demonstrates many bad micro-level coding practices based on PEP 8 guidelines.
# Use the black formatter to format this file.

import os,sys 

def calculate_total(price,quantity): 
    total=price*quantity
    discount=0.1 
    final_total=total*(1-discount) 
    return final_total

def Get_Shipping_Cost(price,quantity,shipping_cost_percentge=0.05):
    result=(price*quantity)*shipping_cost_percentge
    return result


def main():
    item_name=input("Enter item name: ")
    price=float(input('Enter price: '))
    quantity=int(input("Enter quantity: "))

    total = calculate_total(price, quantity)

    extra=Get_Shipping_Cost(price, quantity)
    print(f"Total for {item_name}: ${total:.2f}")
    print (f"Extra calculation: {extra}")
    print (f"Cart value: {total + extra}")

if __name__=="__main__":
    main()