from ui.ui import UI
from database import Database
from service import Service

def main():
    """Runs the mainloop of the application"""

    database = Database('test.db')
    service = Service(database)
    app = UI(service)
    app.loop()

if __name__ == '__main__':
    main()
