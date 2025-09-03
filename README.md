# ERP con Odoo - Grupo C

**Entorno de desarrollo:**  
- Máquina virtual: Ubuntu 22.04  
- Sistema operativo: Linux  
- Odoo: versión 18
  
## Integrantes
- Valentina Vargas  
- Lucila Velardez  
- Mateo Rivas  
- Rodrigo Funes  

## Tutor
- Agustín Bordón

## Ramas del repositorio
- `main` - rama principal, contiene la versión estable del proyecto  
- `dev` - rama de desarrollo, para probar y agregar nuevas funcionalidades  

## Instalación / Uso
Este repositorio debe ser incorporado dentro de un entorno Odoo.  
La carpeta del proyecto se ubica, por ejemplo, en:  

Workspace/Odoo 18/odoo/custom/src/curso

(donde `curso` es la carpeta creada para este proyecto).  

**Importante:**  
En el archivo `addons.yaml` de tu entorno Odoo, es necesario agregar la siguiente línea para que el sistema reconozca todas las carpetas dentro de `curso`:  

`
curso:
   "*"
`

Dentro del directorio del proyecto, ejecutar:  

`inv start`

Luego ingresar en el navegador a:  

http://localhost:18069

En la pantalla de login:  
- **Base de datos:** `devel`  
- **Usuario:** `admin`  
- **Contraseña:** `admin`  

## Comandos básicos con `invoke (inv)`

- **Levantar el entorno:**  
  `inv start`  
  Levanta los contenedores del entorno.  

- **Detener el entorno:**  
  `inv stop`  
  Detiene todos los contenedores del entorno.  

- **Reiniciar el entorno:**  
  `inv restart`  
  Detiene los contenedores de Odoo y los vuelve a levantar.  


