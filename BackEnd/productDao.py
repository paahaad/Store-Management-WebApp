from sqlConnection import sql_connection
def all_product(connection):
    cursor = connection.cursor()
    query = ''' SELECT product.productId, product.productName, product.pricePerUnit, unitid.unitName
            FROM product
            INNER JOIN unitid
            ON product.unitId = unitid.unitId   '''
    cursor.execute(query)
    response = []
    for (productId, productName, pricePerUnit, unitName) in cursor:
        response.append(
            {
                'productId' : productId,
                'productName' : productName,
                'pricePerUnit' : pricePerUnit,
                'unitName' : unitName
            }
        )
    return response

def insertNewProduct(connection,product):
    cursor = connection.cursor()
    query = ("INSERT INTO product "
             "(productName, unitId, pricePerUnit)"
             "VALUES (%s, %s, %s)")
    data = (product['productName'], product['unitId'], product['pricePerUnit'])
    cursor.execute(query, data)
    connection.commit()
    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM product where productId=" + str(product_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid


if __name__ == '__main__':
    connection = sql_connection()
    # print(all_product(connection))
    """  print(insertNewProduct(connection, {
        'product_name': 'potatoes',
        'unit_id': '1',
        'price_per_unit': 10
    })) """
    # for x in range(9,21):delete_product(connection, x)
   