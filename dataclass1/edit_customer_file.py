from dataclasses import asdict
from dataclass2_customer_class import ProductData
from load_and_save_file import save_file

def edit_customer_order(choose_customer,temporary_container
    
    status_found = False
    
    for customer_name,order_detail in temporary_container.items():
                
        if customer_name == choose_customer:
            
            status_found = True
            
            edit_decision =  input("""
            What do you want to edit:
            1.Product
            2.Quantity
            3.Price
            4.Detail
            0.Exit
            """)
            if edit_decision == '1':
                edited_product_variable = input("Insert the product name(0 for cancel): ")
                
                if edited_product_variable == '0':
                    
                    return
                
                customer_data = ProductData(
                    name=edited_product_variable,
                    quantity=order_detail['quantity'],
                    price=order_detail['price'],
                    detail=order_detail['detail']
                )
                
                temporary_container[choose_customer] = asdict(customer_data)
        
                save_file(temporary_container,'customers_data_file')
                
                print(temporary_container)
                
            elif edit_decision == '2':
                
                edited_quantity_variable = input("Insert the quantity(0 for cancel): ")
                
                if edited_quantity_variable == '0':
                    
                    return
                
                customer_data = ProductData(
                    name=order_detail['name'],
                    quantity=int(edited_quantity_variable),
                    price=order_detail['price'],
                    detail=order_detail['detail']
                )
                
                temporary_container[choose_customer] = asdict(customer_data)
        
                save_file(temporary_container,'customers_data_file')
                
                print(temporary_container)
                
            elif edit_decision == '3':
                
                edited_price_variable = input("Insert the product price(0 for cancel): ")
                
                if edited_price_variable == '0':
                    
                      return
                
                customer_data = ProductData(
                    name=order_detail['name'],
                    quantity=order_detail['quantity'],
                    price=float(edited_price_variable),
                    detail=order_detail['detail']
                )
            
                temporary_container[choose_customer] = asdict(customer_data)
        
                save_file(temporary_container,'customers_data_file')
            
            elif edit_decision == '4':
                
                edited_detail_variable = input("Insert the product detail(0 for cancel): ")
                
                if edited_detail_variable == '0':
                    
                    return
                
                customer_data = ProductData(
                    name=order_detail['name'],
                    quantity=order_detail['quantity'],
                    price=order_detail['price'],
                    detail=edited_detail_variable
                )
            
                temporary_container[choose_customer] = asdict(customer_data)
        
                save_file(temporary_container,'customers_data_file')
            
            elif edit_decision == '0':
                
                break
            
            else:
                print("Invalid menu.")
            
                
    if not status_found:
        print(f"There is no customer name: {choose_customer}.")
