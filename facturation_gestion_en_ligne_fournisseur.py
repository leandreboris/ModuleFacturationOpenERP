# -*- coding: utf-8 -*-
from openerp.osv import osv,fields
import openerp
class facturation_gestion_en_ligne_fournisseur(osv.osv):
  _name='facturation_gestion_en_ligne.fournisseur'
  _columns={
        'nomBanque':fields.char('Nom de la banque', size=128),
		'numCompte':fields.char('Numéro du compte', size=128),
		'codeswift':fields.char('Code SWIFT', size=128),
		'pays':fields.char('Pays', size=128),
		'telBanque':fields.integer('Téléphone'),
		'emailBanque':fields.char('E-mail', size=128),
		'nomContact':fields.char('Nom', size=128),
		'fonctionContact':fields.char('Fonction', size=128),
		'emailContact':fields.char('E-mail', size=128),
		'mobileContact':fields.integer('Mobile'),
		'telContact':fields.integer('Téléphone'),
		'soldeInitial':fields.integer('Solde initial'),
		'delaiLivraison':fields.integer('Délai de livraison'),
		'creditAccorde':fields.integer('Crédit accordé'),
        'codeFournisseur': fields.char('Code du fournisseur', size=128),
        'nomEntreprise': fields.char('Nom entreprise', size=128),
        'typeFournisseur': fields.char('Type de fournisseur', size=128),
        'ice':fields.char('ICE', size=128),
		'tel':fields.integer('Téléphone'),
		'mobile':fields.integer('Mobile'),
		'email':fields.char('E-mail', size=128),
		'siteInternet':fields.char('site Internet', size=128),
        'adrersse':fields.char('Adresse', size=128),
		'codePostal':fields.integer('Code postal'),
        'ville':fields.char('Ville', size=128),
		'pays':fields.char('Pays', size=128),
		'famillefournisseur':fields.selection((
                                       ('test','Test'),
                                       ('test','Test'),
                                      ),'Fammille de fournisseur',require=True),
		'devise':fields.selection((
                                       ('test','Test'),
                                       ('test','Test'),
                                      ),'Devise utilisée',require=True),
		'adressReception':fields.selection((
                                       ('test','Test'),
                                       ('test','Test'),
                                      ),'Adresse de récéption',require=True),							  
		'echancierPaiment':fields.selection((
                                       ('test','Test'),
                                       ('test','Test'),
                                      ),'Echéancier de payement',require=True),
		'modePaiment':fields.selection((
                                       ('test','Test'),
                                       ('test','Test'),
                                      ),'Mode de paiment préféré',require=True),
		'modeLivraison':fields.selection((
                                       ('test','Test'),
                                       ('test','Test'),
                                      ),'Mode livraison péférée',require=True),
		}
facturation_gestion_en_ligne_fournisseur()