import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="app.log",
                    filemode="a",
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('debug message')
logging.info('info message')
logging.warning('warn message')
logging.error('error message')
logging.critical('critical message')
while True:
    file = input("Enter to open your file: ")
    if file == "q" or file == "Q":
        exit(0)
    try:
        with open(file, "r") as f:
            print(f"{file} selected.")
            print(f.read())
        break
    except FileNotFoundError:
        print("Wrong file or file path")
    except UnicodeDecodeError:
        print(f"Impossible open to file {file}")


