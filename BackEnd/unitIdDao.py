from sqlConnection import sql_connection

def getUnitName(connection):
    cursor = connection.cursor()
    query = ('Select * from unitId')
    cursor.execute(query)
    response =[]
    for (unitId, unitName) in cursor:
        response.append(
            {
                'unitId':unitId,
                'unitName':unitName
            }
        )
    return response
if __name__ == '__main__':
    connection = sql_connection()
    print(getUnitName(connection))