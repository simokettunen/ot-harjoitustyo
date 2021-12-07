from ui.ui import UI
from database import Database
from service import Service

def main():
    """Run the mainloop of the program"""
    database = Database('test.db')
    service = Service(database)
    app = UI(service)
    app.loop()

if __name__ == '__main__':
    main()
