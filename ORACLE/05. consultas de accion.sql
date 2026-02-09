--queremos insertar un nuevo departamento
--todos sus datos
insert into DEPT values (50, 'PYTHON', 'ALCOBENDAS');
select * from DEPT;
insert into DEPT(DEPT_NO, LOC) values (51, 'ALICANTE');
--COMMIT
SELECT * FROM PLANTILLA;

select max(EMPLEADO_NO) + 1 from PLANTILLA;
--9902
insert into PLANTILLA
(HOSPITAL_COD, SALA_COD, APELLIDO, FUNCION, TURNO, SALARIO, EMPLEADO_NO)
values (22, 6, 'LOPEZ', 'ENFERMERA', 'T', 150000, (select max(EMPLEADO_NO) + 1 from PLANTILLA ));
rollback;
--delete from PLANTILLA;
delete from PLANTILLA where apellido ='LOPEZ';
--ELINMINAR TODA LA PLANTILLA DEL HOSPILAT EL CARMEN
delete from PLANTILLA where HOSPITAL_COD =
(select HOSPITAL_COD from HOSPITAL where NOMBRE= 'EL Carmen');
--subir en 1 el salario de la plantilla (todos)
update PLANTILLA set SALARIO = SALARIO +1;
update PLANTILLA set FUNCION = 'ENFERMERA', SALARIO= SALARIO + 1
where FUNCION = 'ENFERMERO';
update PLANTILLA SET SALARIO = 
(select SALARIO from PLANTILLA where APELLIDO= 'Karplus w.')
where SALA_COD=4;
--mostrar todas las personas de la plantilla de la sal de psiquiatria
select *from PLANTILLA
where SALA_COD
--Modificar el TURNO a mañana a todos los de la plantilla de la sala de psiquiatria
update PLANTILLA set TURNO='M'
where SALA_COD in --= si solo hay un resultado, in si hay varios
(select SALA_COD from SALA where NOMBRE='psiquiatria');
select SALA_COD from SALA where NOMBRE='psiquiatria'
select * from PLANTILLA;
SELECT * FROM SALA;
--insertar nuevo empleado
SELECT * FROM PLANTILLA;
insert into PLANTILLA
(APELLIDO, SALA_COD, TURNO, EMPLEADO_NO, HOSPITAL_COD)
values ('Cabrales', 4, 'N', (select max(EMPLEADO_NO) + 1 from PLANTILLA ), (select HOSPITAL_COD from HOSPITAL where NOMBRE='El Carmen'));
--BORRAR DE LA PLANTILLA TODAS LAS PERSONAS QUE NO TIENEN UN HOSPITAL ASIGNADO
delet from PLANTILLA where HOSPITAL_COD is 'null' or 
HOSPITAL_COD not in (select HOSPITAL_COD from HOSPITAL);
--Dar de alta con fecha actual al empleado José Escriche Barrera
--como programador perteneciente al departamento de producción. 
-- Tendrá un salario base de 70000 pts/mes y no cobrará comisión. 
select from * EMP;