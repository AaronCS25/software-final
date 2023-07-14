# Examen Final
## Requerimientos
* fastapi
* uvicorn
* httpx
## Pregunta 3
Para el caso de la pregunta 3 algunos cambios que podrían hacerse son:
* Añadir un nuevo atributo booleano (true or false) para verificar si un usuario está habilitado a realizar transferencias.
* Modificar el endpoint "/billetera/pagar" para que no permita realizar transacción alguna si este atributo es false.
* Se tendría que adicionar algunos casos nuevos de prueba, ya que si bien actualmente se valida que la transacción se realice exitosamente, debería validarse que al llegar a los 200 soles ya no se pueda hacer más transferencias.

En general estos cambios en el código no generarían mayores problemas, ya que solo es la adición de un atributo y solo hay un endpoint que lo necesitará a la hora de realizarce, quizás el mayor problema sería el asegurar que este nuevo atributo vuelva a ser true pasado el día y se le permita al usuario hacer nuevas transacciones, si bien el código no se rompería se inabilitaría al usuario el realizar sus transacciones lo que sería una pésima esperiencia de usuario y un problema a arreglar.