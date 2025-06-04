import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model




    def handleCreaGrafo(self, e):
        store = self._view._ddStore.value
        if not store:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(f"Selezionare uno store!!!"))
            self._view.update_page()
            return
        self._model.buildGraph(store)

    def handleCerca(self, e):
        pass

    def handleRicorsione(self, e):

        pass
    def fillDD(self):
        stores = self._model.fillDD()
        for store in stores:
            opzione = ft.dropdown.Option(store)
            self._view._ddStore.options.append(opzione)
        self._view.update_page()

