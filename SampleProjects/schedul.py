import schedule

def print_something():
    print("Hi saleh, this is scheduel!!!")
    
schedule.every(4).seconds.do(print_something)

while True:
    schedule.run_pending()