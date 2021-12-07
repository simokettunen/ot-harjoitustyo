from ui.ui import UI
from database import Database

def main():
    """Run the mainloop of the program"""
    database = Database('test.db')

    app = UI(database)
    app.loop()

if __name__ == '__main__':
    main()
