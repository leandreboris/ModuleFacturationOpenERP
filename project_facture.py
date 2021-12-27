# -*- coding: utf-8 -*-

from openerp.osv import osv,fields
import openerp

class project_facture(osv.osv):
      _name='project.facture'
      

      def _get_cur_function_httc(self, cr, uid, ids, field_name, arg, context):

        return 

      _columns={
        'numfac': fields.char('Numéro', size=128),
        'datefac': fields.date('Date de facturation'),
        'datepaiement': fields.date('Date de paiement'),  
        'total_ht': fields.float('Montant HT'),
        'total_httc': fields.function(_get_cur_function_httc,
                                  method=True,
                                  string='Montant HTTC'),
        'logo': fields.binary('Logo'),
			}

      

project_facture()		