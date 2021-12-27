# -*- coding: utf-8 -*-
import openerp
from openerp.osv import osv,fields


class fgl_facture(osv.osv):
    _name='fgl.facture'
    _columns={
        'num' : fields.char('Numero', size=64),
        'description' : fields.char('Description'),      
        'mode_de_paiement' : fields.char('Mode de paiement'),
        'date_facturation' : fields.char('Date de facturation'),    
        'date_paiement' : fields.char('Date de paiement'),   
        'montant' : fields.char('Montant'),
        'statut' : fields.char('Statut'),
        # 'client' : fields.many2one('fgl.client', 'Client', ondelete='cascade'),
        # 'commande' : fields.many2one('fgl.commande', 'Commande', ondelete='cascade'),   


    }
fgl_facture()


