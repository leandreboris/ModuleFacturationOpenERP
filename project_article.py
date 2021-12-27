# -*- coding: utf-8 -*-

from openerp.osv import osv,fields
import openerp
class project_article(osv.osv):
  _name='project.article'
  _columns={
        'categorie': fields.many2one( 'project.categorie',
                                      'Catégorie',
                                      ondelete='cascade'),

        'nom': fields.char('Nom', size=128),
        'photo': fields.binary('Photo'),
        'prix': fields.float('Prix unitaire'),
        'quantite': fields.integer('Quantité'),

        'achetes': fields.integer('Achetés', size=128),

        'description': fields.text('Description'),

			}
project_article()