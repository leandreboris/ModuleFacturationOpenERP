
from openerp.osv import osv,fields
import openerp
class fgl_client(osv.osv):
  _name='fgl.client'
  _columns={
        'numero': fields.char('Num', size=128),
        'nom': fields.char('Nom', size=128),
        'adresse': fields.char('Adresse', size=128),
		    'tel':fields.integer('Telephone'),
        # 'commandes' : fields.one2many('fgl.commande','id_client','Commandes'),
			}
fgl_client()
