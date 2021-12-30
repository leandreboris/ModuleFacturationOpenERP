# -*- coding: utf-8 -*-

from openerp.osv import osv,fields
import openerp
import datetime

class project_facture(osv.osv):
    _name='project.facture'
    _columns={

        #Informations piece
        'client': fields.one2many('facturation_gestion_en_ligne.client','email','Client', required=True),
        'numero': fields.char('Numéro de facture', size=64),
        'date_de_facture': fields.char('Date de facture *', readonly=True),

        #Informations finances
        'remise_globale': fields.integer('Remise globale'),
        'devise': fields.selection((('EUR','EUR-Euros'), ('DH','DH-Dirhams'), ('USD','Dollars')), 'Devise *', required=True),

        #Echeancier
        'mode_paiement' : fields.selection((('Cash','Cash'),
                                       ('Carte','Carte Banquaire'),
                                        ('Cheque','Chèque'),),'Mode de paiement',required=True),

        #Lignes
        # 'lignes' : fields.many2many('project.ligne',
        #          'lignes_rel',
        #          'facture_id',
        #          'ligne_id',
        #          'Lignes'),



			}

    _defaults = {
        'date_de_facture': lambda *a: datetime.datetime.now().strftime("%m/%d/%Y"), 
    }

    
project_facture()