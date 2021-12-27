# -*- coding: utf-8 -*-
import openerp
from openerp.osv import osv,fields


class fgl_societe(osv.osv):
    _name='fgl.societe'
    _columns={
        'nom' : fields.char('Nom', size=64),
        'adresse' : fields.text('Adresse'),      
        'telephone' : fields.integer('Telephone'),
        'email' : fields.text('Email'),    
        'devise' : fields.selection((('EUR','Euros'), ('DHs','Dirhams')), 'Devise'),
        'site_web' : fields.text('Site web'),
    }
fgl_societe()


