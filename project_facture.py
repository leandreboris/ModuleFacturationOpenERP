# -*- coding: utf-8 -*-
from openerp.osv import osv,fields
import openerp
import datetime
class project_facture(osv.osv):
    _name='project.facture'
    _columns={

        #Informations piece
        'client': fields.one2many('facturation_gestion_en_ligne.client', 'email', 'Client *', size=128, required=True),
        'numero': fields.binary('Numéro de facture', size=64),
        'date_de_facture': fields.char('Date *', readonly=True),
        'description': fields.char('Description'),

        #Informations finances
        'remise_globale': fields.char('Remise '),
        'devise': fields.selection((('EUR','EUR-Euros'), ('DH','DH-Dirhams'), ('USD','US-Dollars')), 'Devise *' ),

        #Echeancier
        'mode_paiement': fields.selection((('cash','Cash'), ('carte','Carte banquaire'), ('cheque','Chèque')), 'Mode de paiement *' ),

        #Lignes
        'lignes' : fields.one2many('project.ligne', 'quantite', 'Lignes *', size=128, required=True),

			}
    _defaults = {
        'date_de_facture':  lambda *a: "Facturé le " + datetime.datetime.now().strftime("%m/%d/%Y"),
    }

    
project_facture()