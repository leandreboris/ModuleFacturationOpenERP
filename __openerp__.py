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
        'views/project_company_view.xml',
        'views/project_numerotation_view.xml',
        'views/marque_view.xml',
        'views/famille_article_view.xml',
        'views/facturation_gestion_en_ligne_client_view.xml',
        'views/facturation_gestion_en_ligne_fournisseur_view.xml',
        'views/categorie_view.xml',
        'views/article_view.xml',
     
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