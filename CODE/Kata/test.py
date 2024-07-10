import unittest
from main import *


class TestGame(unittest.TestCase):

    def deplacement_survivant_sur_la_carte(self):
        self.survivant = Survivant(
            position_x=5, position_y=5, orientation="Nord", sante=100, inventaire=[]
        )
        self.survivant.deplacement_survivant(orientation="Nord", nombre_pas=2)
        self.assertEqual(self.survivant.y, 7)

    def decouverte_ressource_par_le_survivant(self):
        self.survivant = Survivant(
            position_x=5, position_y=5, orientation="Nord", sante=100, inventaire=[]
        )
        self.ressource = Ressource(
            Nom="Eau", Type="Boisson", position_x=6, position_y=5
        )
        self.survivant.position_x = 6
        self.assertEqual(self.survivant.inventaire[0], self.ressource)

    def rencontre_avec_un_zombie_et_perte_de_20_points_de_santé(self):
        self.survivant = Survivant(
            position_x=5, position_y=5, orientation="Nord", sante=100
        )
        self.rencontrerZombie()
        self.assertEqual(self.survivant.sante, 80)

    def la_position_du_survivant_est_enregistre_sur_la_carte(self):
        pass

    def la_position_du_zombie_est_enregistre_sur_la_carte(self):
        pass
