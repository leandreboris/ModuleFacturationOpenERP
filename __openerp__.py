{
    'name' : "Project",
    'version' : '1.0',
    'author' : 'C.Bouhouch & L.B WANGRAWA ',
    'category' : 'ENSAH ERP Mini-projet',
	'sequence' :1,
    'description' : """
                    Facturation et gestion en ligne \n
                    Contient tout le nécessaire pour gérer le commerce d'une société.\n
                    Permet de gérer plusieurs points de commerce et fournit la possibilité de :\n
                    - Gérer facilement les différentes facturations \n
                    - Suivre et gérer efficacement les clients et les différents états des produits.""",
    'website': 'http://www.woinga.com',
    'images' : [],
    'depends' : ['base'],
    'data': [
        'project_societe_view.xml',
        'project_client_view.xml',
        'project_article_view.xml',
        'project_facture_view.xml',
        'project_commande_view.xml',
        'project_societe_wkf.xml',

        ],
    'update_xml': [],
    'js': [],
    'qweb' : [],
    'css':[],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}