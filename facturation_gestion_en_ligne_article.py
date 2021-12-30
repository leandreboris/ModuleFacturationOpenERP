# -*- coding: utf-8 -*-
from openerp.osv import osv,fields
import openerp

class facturation_gestion_en_ligne_article(osv.osv):
  _name='facturation_gestion_en_ligne.article'
  _columns={
        'codeArticle': fields.char('Code de article', size=128),
        'libelleArticle': fields.char('Libellé de article', size=128),
        'stock': fields.boolean('Activer la gestion des stocks'),
        'utilisation': fields.boolean('Ne plus utilisiser cet article'),
        'prixAchat': fields.integer('Pris achat'),
        'prixVente': fields.integer('Pris de vente public'),
        'remise': fields.integer('Remise'),
        'prixVenteClient': fields.integer('Prix de vente'),
        'prixAchatfournisseur': fields.integer('Pris achat'),
        'reference': fields.char('Référence', size=128),
        'description': fields.char('Description', size=128),
        'calcul': fields.char('Calcul par défaut', size=128),
        'tarifDefaut': fields.char('Tarif', size=128),
        'image': fields.binary('image'),
        'calculefamilleArticle': fields.char('Calcule famille article', size=128),
        'idmarque':fields.many2one('facturation_gestion_en_ligne.marque','Marque',ondelete='cascade'),
        'idfamille':fields.many2one('facturation_gestion_en_ligne.famille_article','Famille',ondelete='cascade'),
        'idcategorie':fields.many2one('facturation_gestion_en_ligne.categorie_article','Catégorie',ondelete='cascade'),
        'typeArticle':fields.selection((
                                       ('test','Test'),
                                       ('test','Test'),
                                      ),'Type article',require=True),
		'tva':fields.selection((
                                       ('test','Test'),
                                       ('test','Test'),
                                      ),'TVA',require=True),
		'devise':fields.selection((
                                       ('test','Test'),
                                       ('test','Test'),
                                      ),'Devise',require=True),
        'type':fields.selection((
                                       ('test','Test'),
                                       ('test','Test'),
                                      ),'Type',require=True),
        }
facturation_gestion_en_ligne_article()