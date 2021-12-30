# -*- coding: utf-8 -*-

from openerp.osv import osv,fields
import openerp
class project_ligne(osv.osv):
    _name='project.ligne'
    _columns={

        #Informations piece
        'article' : fields.one2many('facturation_gestion_en_ligne.article', 'libelleArticle', 'Article *', size=128, required=True),
        'quantite': fields.binary('Quantité', size=64),
        'unite': fields.integer('Unité *', required=True),
			}

    
project_ligne()