from sqlConnection import sql_connection
from datetime import datetime
def insertOrder(connection, order):
    curser = connection.cursor()
    order_query = ("INSERT INTO gs.order "
                "(customerName, datetime, total)"
                "VALUES (%s, %s, %s)")
    order_data = (order['customerName'], datetime.now(), order['total'])
    curser.execute(order_query, order_data)
    orderId = curser.lastrowid

    orderDetailsQuery = ("Insert into orderdetails"
                        "(orderId, productId, quantity, totalPrice)"
                        "values (%s, %s, %s, %s)")
    orderDetailsData = []
    for _ in order['orderdetails']:
        orderDetailsData.append([
            orderId,
            int(_['productId']),
            float(_['quantity']),
            float(_['totalPrice'])

        ])
    curser.executemany(orderDetailsQuery, orderDetailsData)
    connection.commit()
    return orderId



def getAllOrder(connection):
    cursor = connection.cursor()
    getAllOrder_query = ("select * from gs.order")
    cursor.execute(getAllOrder_query)

    response =[]
    for (oderId, customerName, datetime, total) in cursor:
        response.append({
            'oderId': oderId,
            'customerName': customerName,
            'datetime' : datetime,
            'total' : total

        })
    return response

if __name__ =='__main__':
    connection = sql_connection()
    '''print(insertOrder(connection,{
        'customerName'  : "mota",
        'total'         : 50,
        'orderdetails'  : [
            {
                'productId' : 1,
                'quantity'  : 2,
                'totalPrice': 50
            },
            {
                'productId' : 3,
                'quantity'  : 3,
                'totalPrice': 100
            }
        ]
    }))'''
    print(getAllOrder(connection))