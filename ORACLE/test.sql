select * from DEPT where DEPT_NO=10;
select APELLIDO, DIRECCION from ENFERMO where INSCRIPCION= 59076;
select * from PLANTILLA;
select APELLIDO, FUNCION from PLANTILLA where TURNO=
delete from ENFERMO where INSCRIPCION=1;
rollback;
commit;
--si no le decimos commit o rollback no se ejecuta
select APELLIDO, OFICIO, DEPT_NO from EMP where DEPT_NO=0
select APELLIDO, OFICIO, DEPT_NO from EMP where DEPT_NO=0 or 1=1;
select OFICIO, APELLIDO, SALARIO from EMP where SALARIO= SALARIO;
update EMP set SALARIO= SALARIO+1 where OFICIO ='DIRECTOR';
update PLANTILLA set SALARIO = SALARIO + 1 where HOSPITAL_COD=19;
select * from EMP;
select * from PLANTILLA;