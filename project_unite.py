# -*- coding: utf-8 -*-

from openerp.osv import osv,fields
import openerp
class project_unite(osv.osv):
    _name='project.unite'
    _columns={
        #Informations 
        'libelle': fields.char('Libellé *', size=128, required=True),
        'description': fields.binary('Description', size=64),
        'prix_unitaire': fields.char('Prix Unitaire *', required=True),

			}
project_unite()