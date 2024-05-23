import threading
from server import WebServer
from controller import CLIController, WebController
from entities import *


def run_web_server(tables, gang, menu, waiter_manager, chefs, kitchen):
    server = WebServer()
    web_controller = WebController(server, tables, gang, menu, waiter_manager, chefs, kitchen)
    web_controller.perform()


def run_cli(tables, gang, menu, waiter_manager, chefs, kitchen):
    cli = CLIController()
    cli.perform(tables, gang, menu, waiter_manager, chefs, kitchen)


if __name__ == '__main__':
    tables = [Table(1), Table(2), Table(3), Table(4), Table(5)]
    gang = Restaurant('Ганг')
    menu = Menu()
    waiter_manager = WaiterManager()
    chefs = [Chef("Рахмат"), Chef("Сора"), Chef("Митахши")]
    kitchen = Kitchen(chefs)

    cli_thread = threading.Thread(target=run_cli, args=(tables, gang, menu, waiter_manager, chefs, kitchen))
    flask_thread = threading.Thread(target=run_web_server, args=(tables, gang, menu, waiter_manager, chefs, kitchen))

    cli_thread.start()
    flask_thread.start()

    cli_thread.join()
    flask_thread.join()
