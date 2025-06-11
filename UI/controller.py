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
        self._view.txt_result.controls.append(ft.Text(f"{interval}, {store}"))
        self._view.update_page()
        self._model.buildGraph(store, interval)
        n, e = self._model.get_info()
        self._view.txt_result.controls.append(ft.Text(f"Grafo correttamente creato!"
                                                      f" Il grafo ha {n} nodi e {e} archi"))

        nodi = self._model.get_all_nodes(self._view._ddStore.value)
        for nodo in nodi:
            opzione = ft.dropdown.Option(text=nodo.order_id)
            self._view._ddNode.options.append(opzione)
        self._view._btnCerca.disabled = False
        self._view.update_page()

    def handleCerca(self, e):
        pass

    def handleRicorsione(self, e):
        pass

    def fillDD(self):
        stores = self._model.fillDD()
        for store in stores:
            opzione = ft.dropdown.Option(key=store.store_id, text=store.store_name)
            #n.b.: devi usare key e non data!!!
            self._view._ddStore.options.append(opzione)
        self._view.update_page()


    def handleCerca(self, e):
        nodo = self._view._ddNode.value
        if not nodo:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(f"Selezionare un nodo di partenza!!!"))
            self._view.update_page()
            return
        listanodi = self._model.getCammino(nodo)
        self._view.txt_result.controls.append(ft.Text(f"Percorso più lungo dal nodo '{nodo}': "))
        for i in listanodi:
            self._view.txt_result.controls.append(ft.Text(f"{i.order_id}"))
        self._view.update_page()


