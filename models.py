from mongoengine import *
from mongoengine import document
from mongoengine.fields import *
from mongoengine.document import *

class product_details(EmbeddedDocument):
    Product_name = StringField()
    Price= IntField()
    quantity= IntField()
    product_img = StringField()
    
class create_order(Document):
    Order_id = StringField()
    UserID = StringField()
    Product_details=ListField(EmbeddedDocumentField(product_details))
    Status= StringField()
    Order_date_time= DateTimeField()
    