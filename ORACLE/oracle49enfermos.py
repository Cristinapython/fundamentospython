
import oracledb

class OracleEnfermos: # nombre de la clase
#delacrar las propiedades en el constructor
    def __init__(self):
        self.connection = oracledb.connect(user="SYSTEM", password="oracle"
                              , dsn="localhost/FREEPDB1")
        
    def eliminarEnfermo(self, inscripcion):#hace referencia al objeto al que estoy trabajando
        #creamos un nuevo cursor entrar
        cursor = self.connection.cursor()
        sql = "delete from ENFERMO where INSCRIPCION =:ins"     
        cursor.execute(sql, (inscripcion,))
        registros= cursor.rowcount
        self.connection.commit()
        #CERRAMOS EL CURSOR: SALIMOS
        cursor.close ()
        return registros
     