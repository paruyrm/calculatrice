class Client:
    def __init__(self, nom, prenom, adresse_complete, email, telephone):
        self.nom = nom
        self.prenom = prenom
        self.adresse_complete = adresse_complete
        self.email = email
        self.telephone = telephone

class Produit:
    def __init__(self, designation, reference, quantite_en_stock, prix):
        self.designation = designation
        self.reference = reference
        self.quantite_en_stock = quantite_en_stock
        self.prix = prix

class ProduitDevis:
    def __init__(self, designation, reference, quantite):
        self.designation = designation
        self.reference = reference
        self.quantite = quantite

class Devis:
    STATUT_EN_COURS = 'EN_COURS'
    STATUT_VALIDE = 'VALIDE'
    STATUT_ANNULE = 'ANNULE'
    
    def __init__(self, numero_devis, client, remise=0, commentaire=''):
        self.numero_devis = numero_devis
        self.statut = self.STATUT_EN_COURS
        self.total = 0.0
        self.remise = remise
        self.commentaire = commentaire
        self.client = client
        self.produits = {}
    
    def ajouter_produit(self, produit, quantite):
        if produit.reference in self.produits:
            if produit.quantite_en_stock >= quantite:
                self.produits[produit.reference].quantite += quantite
                produit.quantite_en_stock -= quantite
            else:
                print(f"Produit {produit.designation} non disponible en quantité suffisante.")
                return
        else:
            if produit.quantite_en_stock >= quantite:
                self.produits[produit.reference] = ProduitDevis(produit.designation, produit.reference, quantite)
                produit.quantite_en_stock -= quantite
            else:
                print(f"Produit {produit.designation} non disponible en quantité suffisante.")
                return
        
        self.calculer_total()
    
    def calculer_total(self):
        self.total = sum(produit.quantite * produit.prix for ref, produit in self.produits.items())
        if self.remise > 0:
            self.total -= self.total * (self.remise / 100)
    
    def valider_devis(self):
        self.statut = self.STATUT_VALIDE

class Magasin:
    def __init__(self, nom, adresse_complete):
        self.nom = nom
        self.adresse_complete = adresse_complete
        self.produits = {}

    def ajouter_produit(self, produit):
        self.produits[produit.reference] = produit

def main():
    # Création du magasin Buy More
    buy_more = Magasin("Buy More", "9000 Burbank Boulevard 91506 Burbank California")
    
    # Ajout des produits
    produits = [
        Produit("Ordinateur portable", "BM-P1500", 12, 499),
        Produit("Téléviseur LCD 40 pouces", "BM-TV40LCD", 8, 399),
        Produit("Téléphone mobile", "BM-BD1000", 5, 299),
        Produit("Console de jeux vidéo", "BM-GX500", 3, 249),
        Produit("Routeur Wi-Fi", "BM-WR100", 15, 49),
        Produit("Imprimante multifonction", "BM-PM2500", 2, 129),
        Produit("Souris optique", "BM-MS200", 30, 9),
        Produit("Clavier USB", "BM-KB100", 25, 15),
        Produit("Câble HDMI", "BM-HD15", 18, 6),
        Produit("Disque dur", "BM-HD1000", 10, 29)
    ]
    
    for produit in produits:
        buy_more.ajouter_produit(produit)

    # Création du client Chuck Bartowski et son devis
    chuck = Client("Bartowski", "Chuck", "1838 Franklin Street, Echo Park à Burbank", "chuck.bartowski@gmail.com", "055-486-987")
    devis_chuck = Devis("D0001", chuck)
    devis_chuck.ajouter_produit(buy_more.produits["BM-BD1000"], 3)
    devis_chuck.ajouter_produit(buy_more.produits["BM-GX500"], 1)
    devis_chuck.ajouter_produit(buy_more.produits["BM-HD15"], 5)
    devis_chuck.ajouter_produit(buy_more.produits["BM-PM2500"], 3)
    devis_chuck.valider_devis()

    print(f"Devis pour {chuck.prenom} {chuck.nom} : {devis_chuck.total}€")
    
    # Création du client Sarah Walker et son devis
    sarah = Client("Walker", "Sarah", "Inconnue", "sarah.walker@gmail.com", "055-486-988")
    devis_sarah = Devis("D0002", sarah)
    devis_sarah.ajouter_produit(buy_more.produits["BM-WR100"], 1)
    devis_sarah.ajouter_produit(buy_more.produits["BM-PM2500"], 1)
    devis_sarah.ajouter_produit(buy_more.produits["BM-MS200"], 1)
    devis_sarah.ajouter_produit(buy_more.produits["BM-KB100"], 1)
    devis_sarah.ajouter_produit(buy_more.produits["BM-P1500"], 1)
    devis_sarah.valider_devis()

    print(f"Devis pour {sarah.prenom} {sarah.nom} : {devis_sarah.total}€")

if __name__ == "__main__":
    main()
