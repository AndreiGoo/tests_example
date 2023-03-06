from dataclasses import dataclass


@dataclass
class Appliances:
    """Класс, хранящий имя категории "Бытовая техника"."""

    appliances: str = "Бытовая техника"


@dataclass
class EmbeddedTechnology:
    """Класс, хранящий имя категории "Встраиваемая техника"."""

    embedded_technology: str = "Встраиваемая техника"


@dataclass
class Hobs:
    """Класс, хранящий имя категории "Варочные панели"."""

    hobs: str = "Варочные панели"


@dataclass
class ElectricHobs:
    """Класс, хранящий имя категории "Варочные панели электрические"."""

    electric_hobs: str = "Варочные панели электрические"
