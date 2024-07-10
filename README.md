##ROMAIN BELHIS

# partielSC

## 1. Forkez ce repo ou suivez son exemple de format dans un repo que vous devez me partager à l'adresse remi.hamy@gmail.com
## Format du nom de repo PartielSoftwareCraftmanship"< Votre NOM PRENOM >"

## 2. Partie questions
#1. Corrigez ce code écrit par le stagiaire de votre équipe qui n’est pas
encore familier avec le métier

public class OrderSystem {
private Map<Integer, List<String>> orderList; // Liste des commandes
public void addNewOrder(Integer customerID, String itemName) {
List<String> items = orderList.getOrDefault(customerID, new ArrayList<>());
items.add(itemName);
orderList.put(customerID, items);
}
public void modifyOrder(Integer customerID, Integer itemIndex, String newItemName) {
List<String> items = orderList.get(customerID);
if (items != null && itemIndex < items.size()) {
items.set(itemIndex, newItemName);
}
}
public void removeOrder(Integer customerID, Integer itemIndex) {
List<String> items = orderList.get(customerID);
if (items != null && itemIndex < items.size()) {
items.remove(itemIndex);
}
}
public void printOrders() {
for (Map.Entry<Integer, List<String>> entry : orderList.entrySet()) {
System.out.println("Customer ID: " + entry.getKey());
System.out.println("Items: " + String.join(", ", entry.getValue()));
System.out.println();
}
}
}


#2. Qu’est ce que du code propre ?

Une code propre est un code qui exprime une intention.
Un code maintenable et évoluable.
Qui respecte de bonne règle de nommage pour les variables, des fonctions qui respectent les principes SOLID.


#3. De votre expérience de l’agilité en entreprise, en vous basant surles piliers du manifeste vu en cours. Que pourriez vous améliorer dans la geson de vos projets ?

De mon exprérience, la règle vu en cours qui me parle le plus c'est : Un code qui exprime bien l'intention, une  meilleur segmentation des fonctions pour une meilleur maintenabilité.
Dans mon métier les documentations sont fortement exhasutive au dela d'une solution opérationnelle qi se comprend d'elle même.
Si nos solutions exprime mieux le métier dans les nommages et la segmentations des fonctions, le support/évolutions seraient beaucoup plus confortable.
La compréhension du métier au centre du développement.

#4.
La classe OrderProcessor fait trop de choses.
Difficile d'ajouter de nouvelles fonctionnalités sans modifier OrderProcessor.
OrderProcessor dépend directement de Database, EmailService, et InventorySystem au lieu de dépendre d'abstractions.

Il serait judicieux de : 
-Ajouter des interfaces : 
    public interface DatabaseService {
        void saveOrder(Order order);
    }
    
    public interface EmailService {
        void sendEmail(String to, String subject, String body);
    }
    
    public interface DiscountStrategy {
        void applyDiscount(Order order);
    }
-D'implementer les interfaces dans des services 
Ex : public class DatabaseServiceDefault implement DatabaseService
Cela permetterai des évolutions sans toucher à processOrder.
-On apelle ensuites les class dans le processOrder.

