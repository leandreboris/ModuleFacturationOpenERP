# -*- coding: utf-8 -*-

from openerp.osv import osv,fields
import openerp
class project_categorie(osv.osv):
      _name='project.categorie'
      _columns={
        'description': fields.text('Description'),
        'nom': fields.char('Categorie', size=128),
			}
project_categorie()		