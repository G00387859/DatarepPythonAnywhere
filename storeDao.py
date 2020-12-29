import mysql.connector
from mysql.connector import cursor
#import MySQLdb as sql_db
#from MySQLdb import cursors
import dbconfig as cfg
import collections


class StoreDao:
    ##mydb = sql_db.connect(
    # Make the connection to my sql databse. 
    # the variables are pull from a congiuration file
    mydb = mysql.connector.connect(  
        host=cfg.mysql['host'],
        user=cfg.mysql['username'],
        password=cfg.mysql['password'],
        database=cfg.mysql['database'])
    
    #insert into the mysql databse
    def insert(self, product):
        try:
            cursor = self.mydb.cursor()
            #build the mysql statement
            sql = "insert into store (productType,productName, productPrice) values (%s,%s,%s)"
            values = [
                product['productType'],
                product['productName'],
                product['productPrice']
            ]
            ret = cursor.execute(sql, values)
            print(ret)
            self.mydb.commit()
            print("done")
            return cursor.lastrowid
        except:
            return "possible database duplicate"
        
    # this method will get query the mysql database to fetchall the data with the table             
    def getAll(self):
        cursor = self.mydb.cursor()
        sql = 'select * from store'
        cursor.execute(sql)
        results = cursor.fetchall()
        #print("results ",results)
        returnArray = []
        for result in results:
            colnames = ['id','productType','productName','productPrice']
            book = {}
            if result:
                for i , colName in enumerate(colnames):
                    value = result[i]
                    book[colName] = value
                #print(book)
            returnArray.append(book)
        return returnArray 
    # this method will get the row from the database table where the id = the product name
    def findById(self, productName):
        try:
            cursor = self.mydb.cursor()
            sql = 'select * from store where productName = %s'
            values = [productName]
            cursor.execute(sql, values)
            results = cursor.fetchone()
            returnArray = []
            if results:
                dictionary = {"id":results[0],"productType":results[1],"productName": results[2],"productPrice": results[3]}
                returnArray.append(dictionary)

            return dictionary
        except:
            return "findById err"
    # this method will update the the row that hold the using the key to access the specif row.
    def update(self, product):
        try:
            cursor = self.mydb.cursor()
            sql = "update store set productType = %s,productPrice = %s where productName = %s"
             #sql = "update books set title = %s, author = %s, price = %s where ISBN = %s"
            values = [
            product['productType'],
            product['productPrice'],
            product['productName']
            ]
            cursor.execute(sql, values)
            print(
                product['productType'],
                product['productName'],
                product['productPrice'])
            self.mydb.commit()
            print("commit")
            return product
        except:
            return "update error"
        
    # delete the row that contains the key product
    def delete(self, productName):
        try:
            cursor = self.mydb.cursor()
            sql = 'DELETE from store where productName = %s'
            values = [productName]
            cursor.execute(sql, values)
            self.mydb.commit()
            return ""
        except:
            return "delete error"

storeDao1 = StoreDao()
