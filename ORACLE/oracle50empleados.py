import oracledb

class OracleEmpleados: # nombre de la clase
#delacrar las propiedades en el constructor
    def __init__(self):
        self.connection = oracledb.connect(user="SYSTEM", password="oracle"
                              , dsn="localhost/FREEPDB1")
        
    def eliminarEmpleado(self, emp_no):#hace referencia al objeto al que estoy trabajando
        #creamos un nuevo cursor entrar
        cursor = self.connection.cursor()
        sql = "delete from EMP where EMP_NO =:num"     
        cursor.execute(sql, (emp_no,))
        registros= cursor.rowcount#para ver los registros
        self.connection.commit()
        #CERRAMOS EL CURSOR: SALIMOS
        cursor.close ()
        return registros
     