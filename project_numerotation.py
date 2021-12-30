# -*- coding: utf-8 -*-

from openerp.osv import osv,fields
import openerp
import datetime
class project_numerotation(osv.osv):

   
    _name='project.numerotation'
    _columns={

        # Codes de base
        'client': fields.char('Client', size=128),
        'fournisseur': fields.char('Fournisseur',  size=128),
        'commerciaux': fields.char('Commerciaux'),
        'article': fields.char('Articles'),
        'famille_articles': fields.char("Famille d'articles"),
        'projet' : fields.char('Projet'),
        'depot': fields.char('Dépots'),
        'ordre_production' : fields.char('Ordre de production'),
        'bon_entree' : fields.char("Bon d'entrée"),
        'bon_sortie' : fields.char("Bon de sortie"),
        'stock': fields.char('Stocks'),   


        # Codes documents clients
        'commande': fields.char('Commande', size=128),
        'devis': fields.char('Devis',  size=128),
        'bon_livraison': fields.char('Bon de livraison'),
        'facture_vente': fields.char('Facture de vente'),
        'avoir': fields.char("Avoirs"),
        'reglement' : fields.char('Règlements'),
        

        # Codes documents fournisseurs
        'commande_fournisseur': fields.char('Commande', size=128),
        'devis_fournisseur': fields.char('Devis fournisseur',  size=128),
        'bon_reception': fields.char('Bon de réception'),
        'facture_achat': fields.char("Facture d'achat"),
        'avoir_fournisseur': fields.char("Avoirs"),
        'reglement_fournisseur' : fields.char('Règlements'),


			}

    _defaults = {
        'client': lambda *a: "CLT1",
        'fournisseur' : lambda *b : "FR1",
        'commerciaux' : lambda *c : "CMR1",
        'article' : lambda *d : "ARTL1",
        'famille_articles' : lambda *e : "FA1",
        'projet' : lambda *f : "PRJ1",
        'depot' : lambda *g : "DP1",
        'ordre_production' : lambda *h : "OP1",
        'bon_entree' : lambda *i : "BE1",
        'bon_sortie' : lambda *j : "BS1",
        'stock' : lambda *k : "STCK1",


        'commande':  lambda *a: "CDV-" + datetime.datetime.now().strftime("%m%d%Y") + "-1",
        'devis':  lambda *a: "DEV-" + datetime.datetime.now().strftime("%m%d%Y") + "-1",
        'bon_livraison':  lambda *a: "BL-" + datetime.datetime.now().strftime("%m%d%Y") + "-1",
        'facture_vente':  lambda *a: "FAC-" + datetime.datetime.now().strftime("%m%d%Y") + "-1",
        'avoir':  lambda *a: "AV-" + datetime.datetime.now().strftime("%m%d%Y") + "-1",
        'reglement' :  lambda *a: "REV-" + datetime.datetime.now().strftime("%m%d%Y") + "-1",


        'commande_fournisseur':  lambda *a: "CDVF-" + datetime.datetime.now().strftime("%m%d%Y") + "-1",
        'devis_fournisseur':  lambda *a: "DEVF-" + datetime.datetime.now().strftime("%m%d%Y") + "-1",
        'bon_reception':  lambda *a: "BLF-" + datetime.datetime.now().strftime("%m%d%Y") + "-1",
        'facture_achat':  lambda *a: "FACF-" + datetime.datetime.now().strftime("%m%d%Y") + "-1",
        'avoir_fournisseur':  lambda *a: "AVF-" + datetime.datetime.now().strftime("%m%d%Y") + "-1",
        'reglement_fournisseur' :  lambda *a: "REVF-" + datetime.datetime.now().strftime("%m%d%Y") + "-1",

    }
project_numerotation()