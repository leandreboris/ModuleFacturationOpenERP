# -*- coding: utf-8 -*-
from openerp.osv import osv,fields
import openerp
class facturation_gestion_en_ligne_client(osv.osv):
  _name='facturation_gestion_en_ligne.client'
  _columns={
        'codeClient': fields.char('Code du client', size=128),
        'nomEntreprise': fields.char('Nom entreprise', size=128),
        'typeClient': fields.char('Type de client', size=128),
		'ice':fields.char('ICE', size=128),
		'tel':fields.integer('Téléphone'),
		'mobile':fields.integer('Mobile'),
		'email':fields.char('E-mail', size=128),
		'siteInternet':fields.char('site Internet', size=128),
		'adrersseFacturation':fields.char('Adresse de facturation', size=128),
		'adrersseLivraison':fields.char('Adresse de livraison', size=128),
		'codePostalFacturation':fields.integer('Code postal'),
		'codePostalLivraison':fields.integer('Code livraison'),
		'villeLivraison':fields.char('Ville', size=128),
		'villeFacturation':fields.char('Ville', size=128),
		'paysFacturation':fields.char('Pays', size=128),
		'paysLivraison':fields.char('Pays', size=128),
		'soldeInitial':fields.char('solde initial', size=128),
		'encoursAutorise':fields.char('Encours autorisé', size=128),
		'nomContact':fields.char('Nom', size=128),
		'fonctionContact':fields.char('Fonction', size=128),
		'emailContact':fields.char('E-mail', size=128),
		'mobileContact':fields.integer('Mobile'),
		'telContact':fields.integer('Téléphone'),
		'commercial':fields.selection((
                                       ('test','Test'),
                                       ('test','Test'),
                                      ),'Commercial',require=True),
        'familleClient':fields.selection((
                                       ('test','Test'),
                                       ('test','Test'),
                                      ),'Fammille de client',require=True),
		'devise':fields.selection((
                                       ('test','Test'),
                                       ('test','Test'),
                                      ),'Devise utilisée',require=True),
        'modeLivraison':fields.selection((
                                       ('test','Test'),
                                       ('test','Test'),
                                      ),'Mode de livraison péférée',require=True),
        'grilleTarif':fields.selection((
                                       ('test','Test'),
                                       ('test','Test'),
                                      ),'Grille de tarif',require=True),
        'echancierPaiment':fields.selection((
                                       ('test','Test'),
                                       ('test','Test'),
                                      ),'Echéancier de payement',require=True),
        'modePaiment':fields.selection((
                                       ('test','Test'),
                                       ('test','Test'),
                                      ),'Mode de paiment préféré',require=True),
        'image':fields.binary('image'),
			}
facturation_gestion_en_ligne_client()