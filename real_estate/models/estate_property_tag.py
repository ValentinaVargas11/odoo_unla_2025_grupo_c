from odoo import models, fields

class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Etiqueta de propiedad'
    
    #Ejercicio 17 uni 2
    _sql_constraints = [
        ("unique_tag_name", "UNIQUE(name)", "El nombre de la etiqueta debe ser unico")
    ]

    name = fields.Char(string="Name", required =True)
   