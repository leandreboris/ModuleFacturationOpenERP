# -*- coding: utf-8 -*-

import openerp
from openerp.osv import osv,fields

class project_societe(osv.osv):

    def _gestion_societe_fcn(self,cr,uid,ids,context=None):
        self.write(cr,uid,ids,{'state':'gestion_societe'})
        return True

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


    _name='project.societe'
    _columns={
        'nom' : fields.char('Nom', size=64),
        'adresse' : fields.text('Adresse'),      
        'telephone' : fields.integer('Telephone'),
        'email' : fields.text('Email'),    
        'devise' : fields.selection((('EUR','Euros'), ('DHs','Dirhams')), 'Devise'),
        'site_web' : fields.text('Site web'),
        'state':fields.selection([
                                            ('gestion_societe','Gestion de société'),
                                            ('gestion_article',"Gestion d'articles"),
                                            ('gestion_client','Gestion de clients'),
                                            ('gestion_commande','Gestion de commandes'),
                                            ('gestion_facturation','Gestion des facturations'),
											],'State',readonly=True),
    }
project_societe()


