import time

def trackTime(funcToBeDecorated):
    def timeTaken():
        print("starting..")
        startTime = int(time.time()*1000)
        funcToBeDecorated()
        endTime = int(time.time()*1000)
        print("Time taken:")
        print(f"Function: {funcToBeDecorated.__name__}, Time Taken: {endTime-startTime}")

    return timeTaken()

@trackTime
def func():
    time.sleep(4)
    print("Ending..")
