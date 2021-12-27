# -*- coding: utf-8 -*-
from openerp.osv import osv,fields
import openerp
class project_commande(osv.osv):
  _name='project.commande'
  _columns={
        'client': fields.many2one('project.client',
                                  'Client',
                                  ondelete='cascade'),
        'panier': fields.many2many('project.article',
                 'Panier_articles',
                 'project.commande.id',
                 'project.article.id',
                 'Panier'),
			}
project_commande()