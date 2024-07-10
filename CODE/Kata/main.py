from pydantic import BaseModel, Field, ValidationError
from typing import List, Literal
from enum import Enum


class Ressource(BaseModel):
    type: Literal["nourriture", "eau", "arme"]


class Direction(Enum):
    Nord = "Nord"
    Sud = "Sud"
    EST = "Est"
    OUEST = "Ouest"


class Carte(BaseModel):
    taille_x: int
    taille_y: int
    liste_ressources: List[Ressource]
    liste_survivant: List[Survivant]
    liste_zombies: List[Zombie]


class Survivant(BaseModel):
    position_x: int
    position_y: int
    orientation: Direction
    sante: int
    inventaire: list[Ressource]

    def deplacement_survivant(self, nombre_pas: int):
        explorer()
        pass

    def enregistre_position_survivant_carte(self, carte: Carte):
        enregistre_carte()
        pass

    def verification_emplacement_survivant_carte(self, carte: Carte):
        pass


class Zombie(BaseModel):
    position_x: int
    position_y: int

    def deplacement_aleatoire_zombie(self):
        pass

    def enregistre_position_zombie_carte(self, carte: Carte):
        enregistre_carte()
        pass


class TypeRessource(Enum):
    ARME = "Arme"
    NOURRITURE = "Nourriture"
    BOISSON = "Boisson"


class Ressource(BaseModel):
    Nom: str
    Type: TypeRessource
    position_x: int
    position_y: int

    def enregistre_position_survivant_carte(self, carte: Carte):
        enregistre_carte()
        pass


def explorer(position_x_nitial: int, position_y_nitial: int, nombre_pas: int):
    pass


def enregistre_carte(entite, carte: Carte):
    pass
