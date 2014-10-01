from ProcessPool import ProcessPool # IMPORT PROCESSPOOL
from time import sleep

def one():
    j = 1
    sleep(2)
    for i in range(1,50000):
        j = j * i
    return j

def two():
    j = 1
    sleep(3)
    for i in range(1,50000):
        j = j * i
    return j

def three():
    j = 1
    sleep(4)
    for i in range(1,50000):
        j = j * i
    return j

def four():
    j = 1
    sleep(1)
    for i in range(1,50000):
        j = j * i
    return j

def five():
    j = 1
    sleep(3)
    for i in range(1,50000):
        j = j * i
    return j

def six():
    j = 1
    sleep(2)
    for i in range(1,50000):
        j = j * i
    return j

def seven():
    j = 1
    sleep(4)
    for i in range(1,50000):
        j = j * i
    return j

def eight():
    j = 1
    sleep(1)
    for i in range(1,50000):
        j = j * i
    return j

def nine():
    j = 1
    sleep(6)
    for i in range(1,50000):
        j = j * i
    return j

def ten():
    j = 1
    sleep(6)
    for i in range(1,50000):
        j = j * i
    return j

def eleven(i):
    for j in range(0, 510):
        print '<div style="background-color:yellow; height:%s*3; width:%s*6; font-size:%s" align="center">%s</div><br><br>' % (j, j, j, i)

def twelve(i):
    for j in range(0, 510):
        print '<div style="background-color:blue; height:%s*3; width:%s*6; font-size:%s" align="center">%s</div><br><br>' % (j, j, j, i)

def thirteen(i):
    for j in range(0, 510):
        print '<div style="background-color:red; height:%s*3; width:%s*6; font-size:%s" align="center">%s</div><br><br>' % (j, j, j, i)

def fourteen(i):
    for j in range(0, 510):
        print '<div style="background-color:green; height:%s*3; width:%s*6; font-size:%s" align="center">%s</div><br><br>' % (j, j, j, i)

def fifteen(i):
    for j in range(0, 510):
        print '<div style="background-color:orange; height:%s*3; width:%s*6; font-size:%s" align="center">%s</div><br><br>' % (j, j, j, i)

def sixteen(i):
    for j in range(0, 510):
        print '<div style="background-color:yellow; height:%s*3; width:%s*6; font-size:%s" align="center">%s</div><br><br>' % (j, j, j, i)

def seventeen(i):
    for j in range(0, 510):
        print '<div style="background-color:blue; height:%s*3; width:%s*6; font-size:%s" align="center">%s</div><br><br>' % (j, j, j, i)

def eighteen(i):
    for j in range(0, 510):
        print '<div style="background-color:red; height:%s*3; width:%s*6; font-size:%s" align="center">%s</div><br><br>' % (j, j, j, i)

def nineteen(i):
    for j in range(0, 510):
        print '<div style="background-color:green; height:%s*3; width:%s*6; font-size:%s" align="center">%s</div><br><br>' % (j, j, j, i)

def twenty(i):
    for j in range(0, 510):
        print '<div style="background-color:orange; height:%s*3; width:%s*6; font-size:%s" align="center">%s</div><br><br>' % (j, j, j, i)

def twentyone(i,j):
    sleep(3)
    return i*j

def twentytwo(i,j):
    sleep(2)
    return i*j

def twentythree():
    sleep(3)
    return "i*j"

def twentyfour(i,j):
    sleep(2)
    return i*j

def twentyfive(i,j):
    sleep(4)
    return i*j

def twentysix():
    sleep(5)
    return "i*j"

def twentyseven(i,j):
    sleep(1)
    return i*j

def twentyeight(i,j):
    sleep(2)
    return i*j

def twentynine():
    sleep(3)
    return "i*j"

def thirty(i,j):
    sleep(2)
    return i*j

"""
    01. fUnctions are defined to perform specific tasks
    02. ProcessPool is instantiated.
    03. Methods are called on the instantiated object.

    ### Methods ###
    ---------------

        01. object.start(process_list, no_of_process_at_a_time, sheduling_time)
            - This will queue and start all the processes and the specified number of processes
              will run at a time. More tasks will be processed and queued according to the scheduling time.

        02. object.start_all(process_list)
            - This will start all the tasks in the process list at once.

        03. object.process_exists(pid)
            - Returns True if process exists and False if it doesnt, takes process identifier (pid) as input.

        04. object.kill_process(pid)
            - Kills the specified process, takes process identifier (pid) as input.

        05. object.status(pid)
            - Returns "Running" or "Stopped" depending upon the current status of the task, takes process identifier
              (pid) as input.


    ### Process list ###
    ----------------------

        01. The process list needs to be in the following format.

                process_list = [functions_with_args]
                functions_with_args = [target_function_name, args_as_tuple, waiting_time]
                target_function_name = function name 
                args_as_tuple = (a,b,c,d,..) etc.
                waiting_time = a number in seconds 
    
        02. Thus, process_list format :

                process_list = [[target_function_name1, (a,b,c,..), waiting_time1], [target_function_name2, (a,b,c,..), waiting_time2], [target_function_name3, (a,b,c,..), waiting_time3], ...]

"""

if __name__ == '__main__':
    first_listing = [[one, (), 4], [two, (), 4], [three, (), 4], [four, (), 4], [five, (), 4], [six, (), 4], [seven, (), 4], [eight, (), 4], [nine, (), 4], [ten, (), 4]]
    first_test    = ProcessPool()
    first_test.start_all(first_listing)
    second_listing = [[twentyone, (10328,23221,), 5], [twentytwo, (53221,73322,), 5], [twentythree, (), 5], [twentyfour, (84321,48234,), 5], [twentyfive, (15238,21327,), 5], [twentysix, (), 5], [twentyseven, (22387,36832,), 5], [twentyeight,  (83262,47326,), 5], [twentynine, (), 5], [thirty, (10,3432,), 5]]
    second_test = ProcessPool()
    second_test.start(second_listing, 4, 5)
    #second_listing = [[eleven, ('eleven',)], [twelve, ('twelve',)], [thirteen, ('thirteen',)], [fourteen, ('fourteen',)], [fifteen, ('fifteen',)], [sixteen, ('sixteen',)], [seventeen, ('seventeen',)], [eighteen, ('eighteen',)], [nineteen, ('nineteen',)], [twenty, ('twenty',)]]