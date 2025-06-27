from nicegui import Client, ui
import app.counter as counter


def startup() -> None:
    counter.create()