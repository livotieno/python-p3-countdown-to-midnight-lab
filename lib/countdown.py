import time

def countdown(num):
    while num >= 0:
        if num == 0:
            print("HAPPY NEW YEAR!")
        else:    
            print(f'{num} SECOND(S)!')
        num-=1
#count_down(9)

def countdown_with_sleep(num):
    while num >= 0:
        if num == 0:
            print("HAPPY NEW YEAR!")
        else:    
            print(f'{num} SECOND(S)!')
        num-=1
        time.sleep(1)
#countdown_with_sleep(10)
