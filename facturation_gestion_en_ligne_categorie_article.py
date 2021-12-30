# -*- coding: utf-8 -*-
from openerp.osv import osv,fields
import openerp
class facturation_gestion_en_ligne_categorie_article(osv.osv):
  _name='facturation_gestion_en_ligne.categorie_article'
  _columns={
        'description': fields.char('Description', size=128),
        'libelle': fields.char('Libellé', size=128),
        
			}
facturation_gestion_en_ligne_categorie_article()