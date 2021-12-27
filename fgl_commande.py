# -*- coding: utf-8 -*-
import openerp
from openerp.osv import osv,fields


class fgl_commande(osv.osv):
    _name='fgl.commande'
    _columns={
        'client' : fields.char('Client', size=64),
        'produits': fields.char('Produits'),    
             
    }
fgl_commande()


