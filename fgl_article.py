# -*- coding: utf-8 -*-
import openerp
from openerp.osv import osv,fields


class fgl_article(osv.osv):
    _name='fgl.article'
    _columns={
        'nom' : fields.char('Nom', size=64),
        'photo' : fields.char('Photo'),    
        'description' : fields.char('Description'),      
        'prix' : fields.char('Prix'),
        'disponibilite' : fields.char('Disponibilité'),   
        'historique' : fields.char('Historique'),
        'categorie' : fields.char("Categorie"),



    }
fgl_article()


