from database.DB_connect import DBConnect
from model.Ordine import Ordine
from model.arco import Arco

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
            result.append((row["store_name"], row["store_id"]))
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
        query = """select o1.order_id as Ordine1, o2.order_id as Ordine2, (select sum(t.quantity)
        														from order_items t
        														where t.order_id = o1.order_id) 	
        													    + 
        													    (select sum(t.quantity)
        														from order_items t
        														where t.order_id = o2.order_id)	
        													    as weight
        from orders o1, orders o2
        where o2.store_id = %s
        and o1.store_id = %s
        and o1.order_id <> o2.order_id 
        and o1.order_date > o2.order_date 
        and ABS(datediff(o1.order_date, o2.order_date)) < %s"""

        cursor.execute(query, (store,store,interval))
        for row in cursor:
            result.append(Arco(idMap[row["Ordine1"]], idMap[row["Ordine2"]], row["weight"]))
        cnx.close()
        cursor.close()
        return result



