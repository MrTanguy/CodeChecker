class display:

    def __init__(self, window):
        window.title("CodeChecker")
        window.config(background='#282828')
        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()
        window.geometry("%dx%d" % (width, height))