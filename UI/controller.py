import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model




    def handleCreaGrafo(self, e):
        self._view.txt_result.controls.clear()
        store = self._view._ddStore.value
        opzioni = self._model.fillDD()
        for opzione in opzioni:
           if store == opzione[0]:
               codice = opzione[1]

        if not store:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(f"Selezionare uno store!!!"))
            self._view.update_page()
            return
        try:
            interval = int(self._view._txtIntK.value)
            if interval <= 0:  # eventualmente, puoi anche controllare se è > 0
                raise ValueError("Intervallo deve essere maggiore di zero")
                return
        except (ValueError, TypeError):
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Inserire un numero intero valido e maggiore di 0!"))
            self._view.update_page()
            return
        self._view.txt_result.controls.append(ft.Text(f"{interval}, {codice}"))
        self._view.update_page()
        self._model.buildGraph(codice, interval)
        n, e = self._model.get_info()
        self._view.txt_result.controls.append(ft.Text(f"Grafo correttamente creato!"
                                                      f" Il grafo ha {n} nodi e {e} archi"))
        self._view.update_page()

    def handleCerca(self, e):
        pass

    def handleRicorsione(self, e):

        pass
    def fillDD(self):
        stores = self._model.fillDD()
        for store in stores:
            opzione = ft.dropdown.Option(text=store[0], data=store[1])
            self._view._ddStore.options.append(opzione)
            self._view._ddStore.value = store[1]  # Imposta il valore a un ID, NON al testo

        self._view.update_page()

