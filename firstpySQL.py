import mysql.connector
import csv

mydatabase = mysql.connector.connect(host='localhost',
                                     user='root',
                                     passwd='')
mycursor = mydatabase.cursor()
db = "CREATE DATABASE electronic"
tb = "CREATE TABLE items (SID INTEGER UNIQUE, ITEM_NAME CHAR(50), UNITS INTEGER, RATE INTEGER, MARKET_RATE INTEGER, TOTAL INTEGER)"




class Main():
    def __init__(self):
        try:
            mycursor.execute(db)
            print('New Database Created : Electronics')

        except:
            print('Using existing Database : Electronics')

        mycursor.execute("USE electronic")

        try:
            mycursor.execute(tb)
            print('New Table created : Items')
        except:
            print('Using existing table : Items')

    def drop_table(self):
        i = input('Deleted Tables cannot be retrieved back\nAre you sure (y/n) ')
        if i == 'y':
            try:
                mycursor.execute("DROP TABLE items")
                print('Table deleted')
            except:
                print('Cannot delete table')
        else:
            print('Cancelled')

    def drop_db(self):
        i = input('Deleted Database cannot be retrieved back\nAre you sure (y/n) ')

        if i == 'y':
            try:
                mycursor.execute("DROP DATABASE electronic")
                print('Database deleted')
            except:
                print('Cannot delete Database')
        else:
            print('Cancelled')

    def desc_table(self):
        mycursor.execute("DESC items")
        out = mycursor.fetchall()
        for i in out:
            print(i)

    def insert_row(self):
        formula = "INSERT INTO items (SID, ITEM_NAME, UNITS, RATE, MARKET_RATE, TOTAL) VALUES (%s,%s,%s,%s,%s,%s)"
        # check_first = "INSERT INTO items (SID) VALUES (%s)"
        try:
            s = int(input('New Serial No: '))
            # mycursor.execute(check_first, (s,))
            n = input('Component Name: ')
            r = int(input('Rate per unit: '))

            mrp = int(input("Enter the market rate: "))
            u = int(input('Number of units: '))
            t = mrp * u

            mycursor.execute(formula, (s, n, u, r, mrp, t))
            mydatabase.commit()
            print('\nNew record successfully inserted ')
        except:
            print(f'\nSID {s} is already present in table and cannot be over writen directly, plz enter new SID ')

    def del_row(self):

        formula = "DELETE FROM items WHERE SID = %s"
        try:
            i = int(input('Which SID you want to delete '))
            mycursor.execute(formula, (i,))
            mydatabase.commit()
            print(f'\nRemoved SID {i} successfully ')
        except:
            print(f'SID {i} Not found')

    def update_tb(self):
        try:
            i = int(input('Which SID you want to update: '))
            formula1 = "SELECT * FROM items WHERE SID = %s"
            formula2 = "UPDATE items SET NAME = %s WHERE SID = %s"
            formula3 = "UPDATE items SET UNITS = %s , TOTAL = UNITS*MARKET_RATE WHERE SID = %s"
            formula4 = "UPDATE items SET RATE = %s, TOTAL = UNITS*MARKET_RATE WHERE SID = %s"
            formula5 = "UPDATE items SET MARKET_RATE = %s, TOTAL = UNITS*MARKET_RATE WHERE SID = %s"


            mycursor.execute(formula1, (i,))
            a = mycursor.fetchall()
            for o in a:
                print(o)

            ch = int(input('Update 1.Name  2.Units  3.Rate  4.MarketPrice 5.Cancel: '))
            if ch == 1:
                try:
                    n = input('Name: ')
                    mycursor.execute(formula2, (n, i))
                    mydatabase.commit()
                    print('Updated Name ')
                except:
                    print('Failed to update Name ')

            elif ch == 2:
                try:
                    u = int(input('Units: '))
                    mycursor.execute(formula3, (u, i))
                    mydatabase.commit()
                    print('Updated Units ')
                except:
                    print('Failed to update Units ')

            elif ch == 3:
                try:
                    r = int(input('Rate: '))
                    mycursor.execute(formula4, (r, i))
                    mydatabase.commit()
                    print('Updated Rate ')
                except:
                    print('Failed to update Rate ')

            elif ch == 4:
                try:
                    mrp = input('MarketPrice: ')
                    mycursor.execute(formula5, (mrp, i))
                    mydatabase.commit()
                    print('Updated ')
                except:
                    print('Failed to update')

            else:
                print('Cancelled ')


        except:
            print(f'Cannot Update at SID {i}')

    def fetch_sid(self):
        i = int(input('Which SID you want to fetch: '))
        formula1 = "SELECT * FROM items WHERE SID = %s"
        mycursor.execute(formula1, (i,))
        a = mycursor.fetchall()
        for o in a:
            print(o)

    def show_table(self):
        try:
            mycursor.execute("SELECT * FROM items")
            a = mycursor.fetchall()
            for o in a:
                print(o)
        except:
            print('No table found ')

    def sort_table(self):
        new_ls = []
        try:
            mycursor.execute("SELECT * FROM items ORDER BY SID")

            out = mycursor.fetchall()
            for i in out:
                new_ls.append(i)

            try:
                mycursor.execute("DROP TABLE items")
                print("\nTable deleted !!!")
                mycursor.execute(tb)
                print('Once again students table created !!!')
                # print(f'\n{new_ls}')
                formula = "INSERT INTO items (SID, ITEM_NAME, UNITS, RATE, MARKET_RATE, TOTAL) VALUES (%s,%s,%s,%s,%s,%s)"
                print("inserting ...")
                for j in range(0, len(new_ls)):
                    # print(new[j])
                    mycursor.execute(formula, new_ls[j])
                    mydatabase.commit()

            except:
                print("Unable to delete and Sort data according to SID !!!")

            finally:
                print('Sorted by SID ')
                print('Stored the data in CSV file')
                new.show_table()


        except:
            print("Cannot perform sorting !!!")

    def export_sorted(self):
        new_ls = []
        try:
            mycursor.execute("SELECT * FROM items ORDER BY SID")

            out = mycursor.fetchall()
            for i in out:
                new_ls.append(i)

            try:
                mycursor.execute("DROP TABLE items")
                # print("\nTable deleted !!!")
                mycursor.execute(tb)
                # print('Once again students table created !!!')
                # print(f'\n{new_ls}')
                formula = "INSERT INTO items (SID, ITEM_NAME, UNITS, RATE, MARKET_RATE, TOTAL) VALUES (%s,%s,%s,%s,%s,%s)"
                # print("inserting ...")
                for j in range(0, len(new_ls)):
                    # print(new[j])
                    mycursor.execute(formula, new_ls[j])
                    mydatabase.commit()

                """Creating CSV and storing the data from MYSQL into CSV"""
                with open("C:\\Users\\acer\\Desktop\\output_sorted.csv", "w") as output:
                    output_dt = csv.writer(output, delimiter=',')
                    output_dt.writerow(['SID', 'ITEM_NAME', 'UNITS', 'RATE(RS)', 'MARKET_RATE(RS)', 'TOTAL(RS)'])
                    for i in new_ls:
                        output_dt.writerow(i)

            except:
                print("Unable to delete and Sort data according to SID !!!")

            finally:
                print('Stored the data in CSV file')
                # new.show_table()


        except:
            print("Cannot perform sorting !!!")

    def export_unsorted(self):
        new_ls = []
        try:
            mycursor.execute("SELECT * FROM items")
            a = mycursor.fetchall()
            for o in a:
                new_ls.append(o)
                print(o)

            """Creating CSV and storing the data from MYSQL into CSV"""
            with open("C:\\Users\\acer\\Desktop\\output_unsorted.csv", "w") as output:
                output_dt = csv.writer(output, delimiter=',')
                output_dt.writerow(['SID', 'ITEM_NAME', 'UNITS', 'RATE(RS)', 'MARKET_RATE(RS)', 'TOTAL(RS)'])
                for i in new_ls:
                    output_dt.writerow(i)
        except:
            print('Cannot perform action ')


new = Main()
new.export_sorted()