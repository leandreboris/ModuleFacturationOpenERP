# -*- coding: utf-8 -*-

from openerp.osv import osv,fields
import openerp
class project_client(osv.osv):
  _name='project.client'
  _columns={
        'numclient': fields.char('Numéro', size=128),
        'nomclient': fields.char("Nom d'identification", size=128),
        'adresseclient': fields.char('Adresse', size=128),
		    'telclient':fields.integer('Téléphone'),
        'commandes':fields.one2many('project.commande','panier', 'Commandes',ondelete='cascade'),
        'photo' : fields.binary('Photo'),
			}
project_client()