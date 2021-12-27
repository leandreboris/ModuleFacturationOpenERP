# -*- coding: utf-8 -*-

from openerp.osv import osv,fields
import openerp
class project_article(osv.osv):


  def _gestion_article_fcn(self,cr,uid,ids,context=None):
        self.write(cr,uid,ids,{'state':'gestion_article'})
        return True

  def _gestion_client_fcn(self,cr,uid,ids,context=None):
        self.write(cr,uid,ids,{'state':'gestion_client'})
        return True

  def _gestion_commande_fcn(self,cr,uid,ids,context=None):
        self.write(cr,uid,ids,{'state':'gestion_commande'})
        return True

  def _gestion_facturation_fcn(self,cr,uid,ids,context=None):
        self.write(cr,uid,ids,{'state':'gestion_facturation'})
        return True


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
        'state':fields.selection([
                                            ('gestion_article',"Gestion d'articles"),
                                            ('gestion_client','Gestion de clients'),
                                            ('gestion_commande','Gestion de commandes'),
                                            ('gestion_facturation','Gestion des facturations'),
											],'State',readonly=True),

			}
project_article()