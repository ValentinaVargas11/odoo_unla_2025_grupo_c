from odoo import models, fields

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Tipo'

    #Ejercicio 17 uni 2
    _sql_constraints = [
        ("unique_type_name", "UNIQUE(name)", "El nombre de la etiqueta debe ser unico")
    ]

    name = fields.Char(string="Tipo de Propiedad", required =True)
   