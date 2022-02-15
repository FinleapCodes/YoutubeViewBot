import webbrowser, time
url = input("Enter url: ")
duration = input("Enter duration: ")
while True:
    webbrowser.open_new(url)
    time.sleep(int(duration))

    
