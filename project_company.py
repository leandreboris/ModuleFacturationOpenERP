# -*- coding: utf-8 -*-

from openerp.osv import osv,fields
import openerp
class project_company(osv.osv):

    _name='project.company'
    _columns={

        'name': fields.char('Nom *', size=128, required=True),
        'logo': fields.binary('Importer votre Logo', size=64),
        'adresse': fields.char('Adresse *', required=True),
        'adresse_complement': fields.char('Téléphone Fixe'),
        'code_postal': fields.char('Code postal'),
        'ville': fields.char('Ville'),
        'pays' : fields.char('Pays'),
        'tel': fields.char('Téléphone'),
        'mobile': fields.char('Mobile *', required=True),
        'email': fields.char('Email *', required=True),
        'site_web': fields.char('Site web'),
        
        'forme_juridique': fields.char('Forme juridique', size=128),
        'capital': fields.char('Capital', size=128),
        'numrc': fields.char('Numéro RC', size=64),
        'numif': fields.char('Numéro IF'),
        'numtp': fields.char('Numéro TP'),
        'numice': fields.char('Numéro ICE'),
        'numcnss': fields.char('Numéro CNSS'),
        'devise': fields.selection((('EUR','EUR-Euros'), ('DH','DH-Dirhams'), ('USD','Dollars')), 'Devise *', required=True),
        'theme' : fields.char('Thème'),
			}

    _sql_constraints = [
        ('name_unique', 'unique(name)',  'Erreur ! On ne peut avoir deux sociétés de mêmes noms !'),
    ]
project_company()