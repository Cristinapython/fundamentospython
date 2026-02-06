--QUIERO VISUALIZAR EL APELLIDO, ESPECIALIDAD 
--, NOMBRE DEL HOSPITAL, DIRECCION DE HOSPITAL DE LOS DOCTORES
select DOCTOR.APELLIDO, DOCTOR.ESPECIALIDAD
, HOSPITAL.NOMBRE, HOSPITAL.DIRECCION
from DOCTOR
inner join HOSPITAL
on DOCTOR.HOSPITAL_COD = HOSPITAL.HOSPITAL_COD;
--MOSTRAR EL NUMERO DE PERSONAS POR CADA DEPARTAMENTO 
--DE LOS EMPLEADOS
select count(*) as PERSONAS, DEPT_NO
from EMP
group by DEPT_NO;
--MOSTRAR EL NUMERO DE PERSONAS PPR CADA NOMBRE DE DEPARTAMENTO 
-- DE LOS EMPLEADOS
select count(*) as PERSONAS, DEPT.DNOMBRE
from EMP
inner join DEPT
on EMP.DEPT_NO = DEPT.DEPT_NO
group by DEPT.DNOMBRE;

select distinct DEPT_NO from EMP;
select * from DEPT;

--CREAR UN EMPEADO SIN DEPARTAMENTO
--111- alumno - 50

--MOSTRAS EL APELLIDO , OFICIO, NOMBRE DEL DEEPARTAM,ENTO , LOCALIDAD DE LOS EMP
select EMP.APELLIDO, EMP.OFICIO
, DEPT.DNOMBRE, DEPT.LOC
from EMP
inner join DEPT
on EMP.DEPT_NO = DEPT.DEPT_NO;
--RIGTH JOIN: PRODUCCION GRANADA
select EMP.APELLIDO, EMP.OFICIO
, DEPT.DNOMBRE, DEPT.LOC
from EMP
right join DEPT
on EMP.DEPT_NO = DEPT.DEPT_NO;
--LEFT JOIN



--FULL JOIN : PRODUCCION GRANADA
--ALUMNO AVIADOR
select EMP.APELLIDO, EMP.OFICIO
, DEPT.DNOMBRE, DEPT.LOC
from EMP
full join DEPT
on EMP.DEPT_NO = DEPT.DEPT_NO;
--cross join : producto cartesiano
select EMP.APELLIDO, EMP.OFICIO
, DEPT.DNOMBRE, DEPT.LOC
from EMP
cross join DEPT;

--suma salarial de cada persona de la plantilla por cada Nombre de hospital
--select count(*) as PERSONAS, DEPT.DNOMBRE
--from EMP
--inner join DEPT
--on EMP.DEPT_NO = DEPT.DEPT_NO
--group by DEPT.DNOMBRE;
select sum(PLANTILLA.SALARIO) as SUMASALARIAL, HOSPITAL.NOMBRE
from PLANTILLA
inner join HOSPITAL
on HOSPITAL.HOSPITAL_COD = PLANTILLA.HOSPITAL_COD
group by HOSPITAL.NOMBRE;
--nº de empleados que trabajan en cada localidad
select count(EMP.EMP_NO) as EMPLEADOS, DEPT.LOC
from EMP
right join DEPT
on EMP.DEPT_NO = DEPT.DEPT_NO
group by DEPT.LOC;
--mostrar apellido, funcion, nombre de hospital,
--direccion hospital
--nombre de la sala de los empleados de la plantilla

select PLANTILLA.APELLIDO, PLANTILLA.FUNCION
, HOSPITAL.NOMBRE, HOSPITAL.DIRECCION
, SALA.NOMBRE
from PLANTILLA
inner join HOSPITAL
on PLANTILLA.HOSPITAL_COD = HOSPITAL.HOSPITAL_COD
inner join SALA
on HOSPITAL.HOSPITAL_COD = SALA.HOSPITAL_COD
and PLANTILLA.SALA_COD = SALA.SALA_COD;


 --Seleccionar el apellido, oficio, salario, 
 --numero de departamento y su nombre, de todos los 
 --empleados cuyo salario sea mayor de 300000
select EMP.APELLIDO, EMP.OFICIO, EMP.SALARIO
,DEPT.DEPT_NO, DEPT.DNOMBRE
from EMP 
inner join DEPT
on EMP.DEPT_NO = DEPT.DEPT_NO
where EMP.SALARIO > 300000;
--Mostrar todos los nombres de Hospital con sus nombres de salas correspondientes.
select HOSPITAL.NOMBRE as NOMBRE_HOSPITAL
,SALA.NOMBRE as NOMBRE_SALA
from HOSPITAL
inner join SALA
on HOSPITAL.HOSPITAL_COD = SALA.HOSPITAL_COD;
--Calcular cuántos trabajadores de la empresa hay en cada ciudad.
select count(EMP.EMP_NO) as TRABAJADORES, DEPT.LOC as CIUDAD
from EMP
right join DEPT
on EMP.DEPT_NO = DEPT.DEPT_NO
group by DEPT.LOC;
--Visualizar cuantas personas realizan cada 
--oficio en cada departamento mostrando el nombre
-- del departamento.
select count (EMP.EMP_NO) as PERSONAS, EMP.OFICIO
, DEPT.DNOMBRE as DEPARTAMENTO
from EMP
inner join DEPT
on DEPT.DEPT_NO = EMP.DEPT_NO
group by EMP.OFICIO, DEPT.DNOMBRE;
--Contar cuantas salas hay en cada hospital,
-- mostrando el nombre de las salas y el 
--nombre del hospital.
select count(SALA.SALA_COD) as NUMERO_SALAS, HOSPITAL.NOMBRE as HOSPITAL, SALA.NOMBRE as SALA
from HOSPITAL
inner join SALA
on SALA.HOSPITAL_COD = HOSPITAL.HOSPITAL_COD
group by HOSPITAL.NOMBRE, SALA.NOMBRE;




 

