BASE_FARE=4
CHANGE_FARE=0.25
BASE_DISTANCE = 140

TOTAL_FARE=0

def calc_fare(user_input):
    distance=user_input*1000
    fare=BASE_FARE+((distance/140)*0.25)
    return fare


if __name__=='__main__':
    user_input=int(input('Enter your distance travelled in Kilometers:\n\t'))
    TOTAL_FARE=calc_fare(user_input)
    print(f'Hello passenger, Yout fare for the distance of {user_input}Km cost ${TOTAL_FARE}')

