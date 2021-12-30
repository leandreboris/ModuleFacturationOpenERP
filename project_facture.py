# -*- coding: utf-8 -*-

from openerp.osv import osv,fields
import openerp
class project_facture(osv.osv):
    _name='project.facture'
    _columns={

        #Informations piece
        'client': fields.char('Nom *', size=128, required=True),
        'numero': fields.binary('Numéro de facture', size=64),
        'date_de_facture': fields.char('Adresse *', required=True),
        'projet': fields.char('Téléphone Fixe'),

        #Informations finances
        'remise_globale': fields.char('Téléphone Fixe'),
        'devise': fields.char('Téléphone Fixe'),

        #Echeancier
        'mode_paiement' : fields.selection(),
        'date_echeance' : fields.date(),

        #Lignes
        # 'lignes' : fields.many2many(),

			}

    
project_facture()