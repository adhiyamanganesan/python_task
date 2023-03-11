from typing import Union
from models import *
from fastapi import FastAPI,Form,File,UploadFile
from datetime import datetime

app = FastAPI()
connect(db="productdata" , host="localhost" , port=27017)
now = datetime.now()
def user_id():
    user = create_order.objects().count()
    id = "UID"+str(100+user)
    return id
def order_id():
    user = create_order.objects().count()
    id = "ORDID"+str(10000+user)
    return id

@app.post("/api/v1/order-create")
def order_create(Product_name: str = Form(...),Price: int = Form(...),
    quantity: int = Form(...), product_img : UploadFile = File(...)):
    k = []
    s = {
        "Product_name" : Product_name,
        "Price":Price,
        "quantity": quantity
    }
    k.append(s)
    product_data = product_details(
        Product_name = Product_name,
        Price= Price,
        quantity= quantity,
        
    )
    data = create_order(
        Order_id = user_id(),
        UserID = order_id(),
        Status=str(Product_name),
        Order_date_time=now.strftime("%d/%m/%Y %H:%M:%S"),
    )
    data.Product_details.append(product_data)
    data.save()
    return k


@app.get("/api/v1/order")
def get_order_details(order_id: str = Form(),user_id:str = Form()):
    order_details = create_order.objects(Order_id=order_id,UserID=user_id).first()
    #for i in order_details:
    pro_det = []
    Total_amount = 0
    for i in order_details["Product_details"]:
        details ={
            "Product_name" : i["Product_name"],
            "Price" : i["Price"],
            "quantity" : i["quantity"]
        }
        Total_amount = Total_amount + int(i["Price"])
        pro_det.append(details)
    data = {
        "order_id": order_details['Order_id'],
        "user_id" : order_details['UserID'],
        "Product_details":pro_det,
        "Total_amount":Total_amount,
        "status":order_details['Status'],
        "Order_date_time":order_details['Order_date_time']
    }
    return data

@app.put("/api/v1/order-update")
def order_update(order_id: str = Form(),user_id:str = Form()):
    order_details = create_order.objects(Order_id=order_id,UserID=user_id).first()
    order_details.update(Status="confirmed",Order_date_time=now.strftime("%d/%m/%Y  %H:%M:%S"))
    return ""