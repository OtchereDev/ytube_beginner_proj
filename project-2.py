first_shipment=10.95
change=2.95

def calc_shipment(user_input):
    if user_input==1:
        return first_shipment
    else:
        return first_shipment+(user_input-1)*change

if __name__=='__main__':
    user_input=int(input('Please enter the quantity of product in your order: \n\t'))
    if user_input!=0:
        total_shipment=calc_shipment(user_input)
        print(f'Your total shipment cost is ${total_shipment}. Thank you')
    else:
        print('Please enter a valid quantity number. Thank you')

        