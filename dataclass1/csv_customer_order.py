import csv


def save_customer_order_data_in_csv(the_excel_file,customer_data):
    with open(the_excel_file, "w", newline= "",encoding="utf-8") as file:
        writing = csv.DictWriter(file, fieldnames=["Customer name","Product name","Quantity","Product price per unit","Product detail","Total price"])
        writing.writeheader()
        writing.writerows(
            {
                "Customer name": cname,
                "Product name": data["name"],
                "Quantity": data["quantity"],
                "Product price per unit": data["price"],
                "Product detail": data["detail"],
                "Total price": data["total_price"],
            }
            for cname, data in customer_data.items()
        )
        
    print("Success.")
