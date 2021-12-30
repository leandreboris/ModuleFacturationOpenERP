# -*- coding: utf-8 -*-

from openerp.osv import osv,fields
import openerp
class project_ligne(osv.osv):
    _name='project.ligne'
    _columns={

        #Informations piece
        'article': fields.char('Nom *', size=128, required=True),
        'quantite': fields.char('Numéro de facture', size=64),
        'unite': fields.char('Adresse *', required=True),
			}

    
project_ligne()