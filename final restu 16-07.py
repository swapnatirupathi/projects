import mysql.connector as db
import datetime
import sqlite3

con=db.connect(user='root',password='Veekshu@16',host='localhost',database='veekshu');
cur=con.cursor()
cur.execute('select * from menu')
data=cur.fetchall()
#print(data)
#cur.close()
#con.close()
#Hotel Management System
#restaurent management system
#admin criteria:
user = 'veekshu'
password = 'chandu@16'
cust = 'sap'
paswrd = '1234567!'
while True:
    print('1.admin')
    print('2.user')
    print('3.exit')
    ch = input('choose a number:')
    if ch.isalpha():
        print('choose correct ans')
    elif ch == 1 :
        login = input('enter user name:')
        password = (input('enter password:'))
        if (login == user) and (password == password):
            while True:
                print('1.add menu')
                print('2.delete menu')
                print('3.moify menu')
                print('4.view all orders')
                print('5.day wise profit')
                print('6.exit')
                print()
                
                choose = int(input('choos a number:'))
                if choose.isalpha():
                    print('choose correct ans')
                elif choose == 1:
                        print('you have choosed to add menu')
                        name = input('which item you want to add: ')
                        category = input('which category you want to add: ')
                        price = input('how much price you want to add: ')
                        
                        cur.execute('insert into menu (name,category,price) values (%s,%s,%s)',(name,category,price));
                        con.commit()
                        print('added item into menu successfully!')
            
                elif choose == 2:
                        print('you have choosed to delete item from menu, which item you wnat to delete now:')
                        item_no = input('please enter the item number: ')
                        cur.execute('delete from menu where item_id =(%s)', (item_no,));
                        con.commit()
                        print('deleted item from menu successfully!')
                        print()

                elif choose == 3:
                        print('you have choosen to modify the item in menu: ')
                        item_name = input('which item do you want to modify, please enter the item number: ')
                        cur.execute('select * from menu where item_id = (%s)',(item_name,))
                        res = cur.fetchone()
                        if res:
                            new_pr = input('enter the price you wnant:')
                            cur.execute('update menu set price = (%s) where item_id = (%s)', (new_pr,item_name))    
                            con.commit()
                            print('modified the price in menu successfully!')
                            print()
                            
                elif choose == 4:
                    con=db.connect(user='root',password='Veekshu@16',host='localhost',database='veekshu');
                    cur=con.cursor()
                    print('you have choosen to view all orders:')
                    usr_ord = cur.execute('select * from ords')
                    rows = cur.fetchall()
                    print(f'{'ord_id':<10} {'item_id':<10} {'user_id':<10} {'quantity':<10} {'ord_date': <10} {'total_price':<10}')
                    for i in rows:
                        print(f'{str(i[0] or ''):<10} {str(i[1] or ''):<10} {str(i[2] or ''):<10} {str(i[3] or ''):<10} {str(i[4] or ''):<10}  {str(i[5] or ''):<10}')
                        print()
                elif choose == 5:
                        print('you have choosen to day-wise profit: ')
                        cur.execute('''
                            SELECT ord_date,
                                   SUM(total_price * quantity) AS day_profit
                            FROM ords
                            GROUP BY ord_date
                            ORDER BY ord_date
                        ''')
                        rows = cur.fetchall()
                        print(f"{'Date':^15}{'Day Wise Profit':^20}")
                        print('-'*100)
                        for i in rows:
                            print(f"{str(i[0]):^15}{str(i[1]):^15}")
                    
                elif choose == 6:
                    n = input(' if you want to close the window say (yes/no):')
                    if n == 'yes':
                        print('exit')
                        break
                        print()

#user ciretria
                            
    elif ch == 2 :
        while True:
                user_name = input('enter your name: ')
                mob_num = input('enter your moblie number: ')
                if len(mob_num) == 10 and mob_num.isdigit() and user_name.isalpha():
                    cur.execute('insert into users (name, mob_num) values (%s,%s)',(user_name,mob_num));
                    con.commit()
                    
                    print('1.view menu')
                    print('2.add items to cart')
                    print('3.modify cart')
                    print('4.bill')
                    choose = int(input('choose a number:'))
                    if choose.isalpha():
                        print('choose correct ans')
                    elif choose == 1:
                        print('you have choosen the view menu:')
                        cur.execute('select * from menu')
                        data = cur.fetchall()
                        print(f'{'item_id':<10}{'name':<20}{'category':<10}{'price':<20}')
                        for i in data:
                            print(f'{i[0]:<10}{i[1]:<20}{i[2]:<10}{i[3]:<20}')
                            print()
                
                    elif choose == 2:
                        print('you have choosen to add item intto cart: ')
                        order = input('Enter the item id: ')
                        quantity = input('Enter quantity: ')
                        user_id = input('Enter user_id: ')
                    
                        if not quantity.isdigit() or int(quantity) <= 0:
                            print("invalid quantity entered.")
                        
                        else:

                            cur.execute('SELECT price FROM menu WHERE item_id = %s', (order,))
                            result = cur.fetchone()
                            if result:
                                price = result[0]
                                total_price = int(quantity)*price
                                now = datetime.datetime.now()
                                cur.execute( 'INSERT INTO ords (item_id, user_id, quantity, ord_date, total_price)VALUES (%s, %s, %s, %s, %s)', (order[0], user_id, quantity, now, total_price))

                                con.commit()
                                print("item successfully added into cart.")#except exception
                                print()

                    elif choose == 3:
                        print('you have choosen to modify the cart: ')
                        item_id = input('Please enter the item id of the item you want to modify:  ')
                        cur.execute('select * from ords where item_id = (%s)',(item_id,))
                        res = cur.fetchall()
                        if res:
                            print(f"item found: {res}")
                            nqty = input("how much quantity you want to modify: ")
                            cur.execute ("update ords set quantity = (%s) where item_id = (%s)",(nqty,item_id))
                            con.commit()
                            print('Quantity updtaed successfully.')
                        else:
                            print('item not found. Please check the item id and try again.')
                            print()

                    elif choose == 4:
                            cur.execute('SELECT * FROM ords')
                            items = cur.fetchall()
                            print('you have choosen to finalize the bill: ')
                        
                            print("\n=== Final Bill ===")
                            subtotal = 0
                        
                            for item in items:
                                name = item[1]
                                quantity = item[2]
                                total_price = item[3]
                                existing_sub = item[5]
                                if existing_sub != None:
                                    item_total = existing_sub
                                else:
                                    item_total = total_price * quantity
                                subtotal += item_total
                                print(f'{name} (x{str(quantity)}) - ₹{item_total:.2f}')
                           
                            print(f"\nSubtotal: ₹{subtotal:.2f}")
                            print("==================")
                            print()


                    elif choose ==5:
                        n = input(' if you want to close the window say (yes/no):')
                        if n == 'yes':
                                print('exit')
                                break
                                print()
                        
                else:
                    print("Invalid input: Make sure mobile number is 10 digits and name contains only alphabets.")
                           
                            
    else:
        print('Invaild input: Make sure you choose only above options.')
