# -*- coding: utf-8 -*-
"""Clase 1 - Actividad.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bgih7Zuj7H7F9uCrJVqvSLB4GyOvjQYK

# Diplomado en Big Data - Introducción a las Herramientas de la Nube

### **Profesor:** Germán Leandro Contreras Sagredo
### **Ayudante:** Valentina Rojas Mercier

## Actividad de la Clase 1: Creación de cuentas y uso de credenciales

En la siguiente actividad, nos dedicaremos a crear una cuenta para Amazon Web Services y Google Cloud. Este proceso es quizás el más "aburrido" que haremos durante el curso, pero es importante llevarlo a cabo para poder hacer uso de las herramientas sin problemas.

Si lo desean, pueden crear un nuevo correo electrónico para ellas, o bien usar el que sea de su preferencia.

**Importante:** Para poder llevar a cabo la creación de las cuentas, es necesario incluir en el proceso una tarjeta de crédito. Si bien les puedo asegurar que no se les hará ningún cobro siempre que respeten las cuotas de la cuenta gratuita, entiendo si prefieren no hacerlo. En ese caso, deben comunicarse conmigo para poder facilitarles credenciales de una cuenta ya creada.

### PASO 1 - Instalar las librerías a utilizar.

Instalamos las librerías para hacer uso de AWS (boto3) y Google Cloud. En el caso de este último, existe una librería por servicio a utilizar. De momento, haremos uso de los servicios de almacenamiento de objetos: S3 y Google Cloud Storage.
"""

!pip install boto3
!pip install google-cloud-storage

"""### PASO 2 - Acceder a *bucket* de S3 y descargar archivo

Para efectos de esta actividad, haremos uso de una cuenta ya creada.

Vamos a acceder a un *bucket* en S3 llamado "introduccion-herramientas-nube-actividad-1", descargar un archivo y mostrarlo en una celda.
"""

import boto3

# Obtenemos el acceso a S3. Aquí incluimos las credenciales a nuestra cuenta.
s3 = boto3.resource(
    's3',
    aws_access_key_id='',
    aws_secret_access_key=''
)

# Accedemos al bucket según su nombre.
bucket = s3.Bucket('introduccion-herramientas-nube-actividad-1')

# Descargamos el archivo. Ingresa el nombre del archivo que desees, respetando
# su formato.
bucket.download_file('ejemplo.gif','yo-bailando.gif')

"""Vemos el archivo a continuación. Cambie el nombre por el del archivo creado."""

from IPython.display import Image
# Escribe aquí el nombre de archivo que hayas escrito.
Image(open('yo-bailando.gif','rb').read())

"""### PASO 3 - Acceder a *bucket* de Cloud Storage y descargar archivo

Para efectos de esta actividad, haremos uso de una cuenta ya creada.

Vamos a acceder a un bucket en Cloud Storage llamado "introduccion-herramientas-nube-actividad-1", descargar un archivo y mostrarlo en una celda. Para ello, antes de ver el código, es necesario descargar las credenciales haciendo uso de lo que acabamos de aprender.
"""

# Descargamos el archivo de credenciales. Ingresa el nombre del archivo que
# desees, respetando su formato.
bucket.download_file('google-credentials.json','credentials.json')

"""Exportamos la ruta de este archivo en una variable de entorno y procedemos a iniciar un cliente de Cloud Storage para obtener el archivo."""

# Desde esta librería podemos configurar nuestras variables de entorno. Cabe
# destacar que aquí le debemos pasar la ruta del archivo, no solo el nombre.
# En este caso basta con el nombre al encontrarse en el mismo directorio.
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'credentials.json'

# Importamos la librería storage.
from google.cloud import storage

# Instanciamos el cliente.
storage_client = storage.Client()

# Nombre del bucket
bucket_name = 'introduccion-herramientas-nube-actividad-1'

# Obtenemos el bucket.
bucket = storage_client.get_bucket(bucket_name)

# Obtenemos el "blob" (archivo)
blob = bucket.blob('ejemplo2.gif')

# Descargamos el archivo. Escojan el nombre que deseen, respetando el formato.
blob.download_to_filename('perro.gif')

"""Vemos el archivo a continuación."""

# Completar con el nombre de archivo escogido.
Image(open('perro.gif','rb').read())

"""### PARTE 4 (Opcional) - Creando nuestras cuentas

A continuación, si lo deseas, veremos cómo crear nuestra cuenta gratuita de
Amazon Web Services y Google Cloud Computing.

#### Cuenta en AWS

1. Ingresa al siguiente enlace y registra tu cuenta: https://portal.aws.amazon.com/billing/signup. Ponle el nombre de cuenta AWS que desees.
![Paso 1](https://drive.google.com/uc?export=view&id=1AMtvSr6VhsgTbf89_SgyWtgjciHfTabR)  
2. Ingresado los datos de cuenta, ingresa tu información personal y dirección. Asegúrate de marcar la casilla "Personal" en modo de uso de AWS.
![Paso 2](https://drive.google.com/uc?export=view&id=1h_QFvDm5lo6vgpHf9fgLyD-9wINUZLD0)  
3. Ingresa tus datos financieros. Solo habrá una retención de 1 dólar como verificación.
![Paso 3](https://drive.google.com/uc?export=view&id=1fQgKV4-rXk8Twb92C7qRoMCeaOzq981a)  
4. Ingresa tu número telefónico e ingresa el código recibido como medio de verificación.
![Paso 4](https://drive.google.com/uc?export=view&id=1NktcATAHvYMmxFZ79a809Ywz3-6odYj-)  

5. Selecciona el tipo de soporte básico. Queremos evitar cobros.
![Paso 5](https://drive.google.com/uc?export=view&id=1zCBpC0iFzJg14YHgrc6W6ZoXr5IQ6T7i)
6. ¡Tu cuenta fue creada exitosamente! Ahora, ingresa a la consola para poder obtener las credenciales.
![Paso 6](https://drive.google.com/uc?export=view&id=12KKWSNpbw0HWSa262zQTSEzxLWC320Rh)    
7. Ingresa a tu cuenta como tipo de usuario "raíz".
![Paso 7](https://drive.google.com/uc?export=view&id=17GilQIS48FHmIO4wjWchlWzvypzcxjKn)  
8. Verás el panel con todos los recursos disponibles de AWS. Ingresa a "IAM".
![Paso 8](https://drive.google.com/uc?export=view&id=1jOEhXYIuzfTYECaMgnjV3c7889hqOOzv)  
9. Dentro del panel de IAM, ingresa al enlace "Mi clave de acceso" en la sección "Enlaces rápidos"
![Paso 9](https://drive.google.com/uc?export=view&id=1p8gWEW1lZIN3LqbYgmSr09E-Lwlqy-Mx)  
10. Presiona el botón "Crear una clave de acceso".
![Paso 10](https://drive.google.com/uc?export=view&id=1o5cpvoptQoHEUbqA7UzePEqY3ZpQRrqn)  
11. Se puede descargar la clave creada, que será un archivo CSV que contiene las credenciales de su cuenta. Pueden desplegarlas también, pero asegúrense de respaldarlas antes de cerrar la ventana, porque en otro caso no podrán verlas de nuevo y tendrán que crear listo.
![Paso 11](https://drive.google.com/uc?export=view&id=1uCOZXe-WOqYHzsJlDta37y-ssnZKhXiD)  
12. Si deciden desplegarlas, se verá de esta forma (claves censuradas a propósito).
![Paso 12](https://drive.google.com/uc?export=view&id=1ZWnFfF97P3fm8R-HcjV5_NUbLQt_7wIr)

¡Listo! Ahora podemos probar rápidamente nuestra cuenta.
"""

# Obtenemos el acceso a S3. Aquí incluimos las credenciales a nuestra cuenta.
# Rellene los datos con su cuenta.
s3 = boto3.resource(
    's3',
    aws_access_key_id='',
    aws_secret_access_key=''
)

# Imprimimos la lista de buckets de nuestra cuenta. No debería haber ninguno.
for bucket in s3.list_buckets():
  print(bucket)

"""#### Cuenta en Google Cloud Computing
1. Ingresa al siguiente enlace con una cuenta Google cualquiera: https://console.cloud.google.com/freetrial/signup. Asegúrate de aceptar las condiciones de servicio.
![Paso 1](https://drive.google.com/uc?export=view&id=1Tr5HO7UaJ4BbmO7bwMdG2bRUHWMpEfKv)  
2. Ingresa tu número telefónico e ingresa el código que recibas mediante SMS.
![Paso 2](https://drive.google.com/uc?export=view&id=1rtlEDse28Nj00VNaMLJjMYpthsNTcKal)  
3. Ingresa tus datos financieros. Usa la configuración utilizada en la imagen.
![Paso 3](https://drive.google.com/uc?export=view&id=1eQSXVaLsyFDiVBJ_ZpcI3fDwPcdEX4Et)  
4. ¡Has creado tu cuenta! Ahora, despliega el menú y selecciona "Cuentas de servicio".
![Paso 4](https://drive.google.com/uc?export=view&id=1NW1QLh8Zmu7J3mNnF6QtErb_531MfTqy)  
![Paso 5](https://drive.google.com/uc?export=view&id=1jT8DFWFfTfI-DBJz7Dy7n1OPqVYMTTAp)
5. En este panel, presiona el botón "CREAR CUENTA DE SERVICIO" y sigue las instrucciones. Puedes ponerle el nombre que gustes a la cuenta, pero selecciona tipo de cuenta "Propietario" para no tener limitantes en uso. Puedes ignorar la tercera opción, más adelante se pueden añadir más personas a la cuenta.
![Paso 6](https://drive.google.com/uc?export=view&id=1n9oC2BfCaV5zMsRMLm8Gq1aZkFyGvt_P)
![Paso 7](https://drive.google.com/uc?export=view&id=1CDV_ueM3sX2IrYg2QNhP-G0gRhFQJPhf)
![Paso 8](https://drive.google.com/uc?export=view&id=18GjUIPD2l0uBq3GPISNOGaRa26TzUHDN)
![Paso 9](https://drive.google.com/uc?export=view&id=16z_kG9cG602TpklOO-NlaWabtHq8B_Yj)
6. Una vez creada la cuenta de servicio, es necesario crearle una clave, seguir instrucciones a continuación (guardando el archivo como JSON).
![Paso 10](https://drive.google.com/uc?export=view&id=1s9K2KYKLqq5jN-gHittk3rvPJxnvHsK3)
![Paso 11](https://drive.google.com/uc?export=view&id=1NdGN2wt41HyzNtUYDJ_tL-L1iSxaScr0)
![Paso 12](https://drive.google.com/uc?export=view&id=1E34MGTRLRDpuLO5fYm-w8JZn2BR-rDGQ)  
![Paso 13](https://drive.google.com/uc?export=view&id=1xlIesjmfOO7juagKf0m8Ru0wNFVuFubG)

¡Listo! Ahora, hagamos uso de estas credenciales y veamos si funciona. Puedes subir el archivo directamente a esta actividad, o bien crear un nuevo *bucket* en S3, subirlo ahí y obtenerlo de ahí. ¡Eres libre de hacerlo como quieras!
"""

# Actualizamos la variable a las nuevas credenciales.
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = ''

# Iniciamos nuevamente el cliente.
storage_client = storage.Client()

# Listamos todos los buckets disponibles (no debería haber ninguno).
for bucket in storage_client.list_buckets():
    print(bucket)