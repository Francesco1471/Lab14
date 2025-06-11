from database.DB_connect import DBConnect
from model.Ordine import Ordine
from model.arco import Arco
from model.store import Store
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
            result.append(Store(**row))
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

    @staticmethod
    def get_all_edges(store, interval, idMap):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        result = []
        query = """select DISTINCT o1.order_id as Ordine1, o2.order_id as Ordine2, 
                                   count(oi.quantity+ oi2.quantity) as weight
                from orders o1, orders o2, order_items oi, order_items oi2 
                where o1.store_id= %s
                and o1.store_id=o2.store_id 
                and o1.order_date > o2.order_date
                and oi.order_id = o1.order_id
                and oi2.order_id  = o2.order_id
                and DATEDIFF(o1.order_Date, o2.order_date) < %s
                group by o1.order_id, o2.order_id"""

        cursor.execute(query, (store,interval))
        for row in cursor:
            result.append(Arco(idMap[row["Ordine1"]], idMap[row["Ordine2"]], row["weight"]))
        cnx.close()
        cursor.close()
        return result



