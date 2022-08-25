import sys
import datetime

data = {}
def display_menu():

    print('1:Arrival of a car')
    print('2:Total no. of cars Arrived')
    print('3:Departure of car')
    
    print('4:Delete record')
    print('5:Exit program')

    ch = int(input('enter choice:'))
    return ch

def add_record():
    
    while True:
        car_no = input('enter car no.:')

        if car_no not in data:
            break
        print('already exists')

    m_name = input('enter model name:')

    arrival_date = datetime.datetime.now()

    departure_date = "None"

    data[car_no] = {'m_name':m_name,'arrival_date':arrival_date,'departure_date':departure_date}




def display():
   
    print('car_no \tmodel \tArrival_date\t\t\tdep_date')
   

    c=1
    for i in data:
        print("{}\t{}\t{}\t{}".format(i,data[i]['m_name'],data[i]['arrival_date'],data[i]['departure_date']))
        print('-------------------------------------')
        c=c+1


def dep_car():

    c_no = input('enter car no:')

    departure_date = datetime.datetime.now()
    
    if c_no in data:
        data[c_no]['departure_date']= departure_date
    else:
        print('car detail not found')

    

def delete():

    c_no = input('enter car no:')

    if c_no in data:
        del data[c_no]
    else:
        print('car detail not found')


    

    
while True:

    m = display_menu()

    if m==1:
        add_record()
    elif m==2:
        display()
    elif m==3:
        dep_car()
    elif m==4:
        delete()
    else:
        sys.exit()
