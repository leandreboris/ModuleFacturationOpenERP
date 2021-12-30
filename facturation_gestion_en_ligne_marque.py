# -*- coding: utf-8 -*-
from openerp.osv import osv,fields
import openerp
class facturation_gestion_en_ligne_marque(osv.osv):
  _name='facturation_gestion_en_ligne.marque'
  _columns={
        'libelle': fields.char('Libellé', size=128),
        'idarticle':fields.one2many('facturation_gestion_en_ligne.article','idmarque',string='Article'),
			}
facturation_gestion_en_ligne_marque()