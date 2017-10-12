import webbrowser, time, sys

def time_construct(break_interval):
    break_interval = time.time() + break_interval
    break_time = time.localtime(break_interval)

    format_time = time.strftime('%H: %M %S %p', break_time)

    return  format_time


def take_a_break(break_interval, url):
    print("opening webbrowser..")
    new = 2

    if url == "":
        url = "https://www.youtube.com/watch?v=Sl2HeP8RlfU"

    if break_interval == "":
        break_interval = 25 * 60

    print ('playing {} at {}'.format(url, time_construct(break_interval)))

    time.sleep(break_interval)

    webbrowser.open(url, new=new)

def main():

    print('''
            At what interval 'in min' would you like to take a break? e.g 1, 25
            press enter to use default 25min
            
            ''')
    if sys.version_info[0] == 2:
        inp = raw_input
    else:
        inp = input
    break_interval = int(inp(">> ")) * 60

    print ('''
        What music would you like to play? provide a url e.g http://www.youtube.com/
        press enter to use default, "you're beautiful by zedd"
    
    ''')
    url = str(inp(">> "))

    while True:
        take_a_break(break_interval, url)


if __name__ == '__main__':

    main()

