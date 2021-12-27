# -*- coding: utf-8 -*-
import openerp
from openerp.osv import osv,fields


class fgl_layout_facture(osv.osv):
    _name='fgl.layout.facture'
    _columns={
        'logo' : fields.char('Logo', size=64),
        'police' : fields.char('Police'),      
        'couleur' : fields.char('Couleur'),
        'facture' : fields.char('Facture'),
       


    }
fgl_layout_facture()


