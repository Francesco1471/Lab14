from dataclasses import dataclass

from model.Ordine import Ordine


@dataclass
class Arco:
    Ordine1: Ordine
    Ordine2: Ordine
    weight: float
