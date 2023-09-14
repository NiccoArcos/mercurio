# Mercurio
Aplicacion de escritorio en proceso de desarrollo que automatiza el envio de correos de buzones coorporativos, chequea los recursos de la infraestructura de exchange, chequea su disponibilidad y genera estadisticas de las pruebas realizadas.
Tecnologias utilizadas: Python (PySide6), QtDesigner.


Desk application in developing process that search automate the send mail on corporative mailboxes, check the resources of exchange's infraestructure, check her availability and generate test's made statistics.
Technology used: Python(PySide), QtDesigner.

Esta aplicacion trabaja con:
1 Modulo de Conexion, el cual trabaja con un metodo de clase que establece la conexion al servidor de correo a través de un contexto SSL.
1 Modulo de Envio, que hereda el metodo de conexion de la clase Conexion para poder ejecutar el envio a través de un metodo de clase.
1 Modulo main donde se encuentra toda la logica de la union entre la UI y las acciones que debe ejecutar la aplicacion segun la opcion seleccionada.
1 Modulo donde se desarrolla toda la UI, este modulo fue confeccionado con la herramienta QTDesigner.
Al no tener una version web y al ser una aplicacion de escritorio trabajo el codigo directamente con PYQT, ya que estoy trabajando con QTDesigner de este modo se puede aprovechar la potencia de toda la variedad de librerias,modulos,objetos que PySide6 provee.


