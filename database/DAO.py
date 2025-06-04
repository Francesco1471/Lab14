from database.DB_connect import DBConnect
from model.Ordine import Ordine


class DAO():

    @staticmethod
    def fillDD():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        result = []
        query = """select *
                    from stores s """
        cursor.execute(query)
        for row in cursor:
            result.append(row["store_name"])
        cnx.close()
        cursor.close()
        return result

    @staticmethod
    def get_all_nodes(store):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        result = []
        query = """select o.*
                    from stores s, orders o
                    where o.store_id = s.store_id
                    and s.store_id = %s """
        cursor.execute(query, (store,))
        for row in cursor:
            result.append(Ordine(**row))
        cnx.close()
        cursor.close()
        return result

