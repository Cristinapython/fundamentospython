select * from DEPT;
select * from EMP;
select DEP_NO, NOMBRES, LOC from DEPT;
select * from EMP order by SALARIO desc;
select * from EMP order by OFICIO desc;
--mostras los empleados del dpt.10
--were CAMPO = VALOR
select * from EMP where DEPT_NO = 10;
--mostrar todos los empleados con oficio director
--Oracle diferencian en sus datos STRING
select * from EMP whwere OFICIO = 'DIRECTOR';
select * from EMP whwere OFICIO = 'director';
--mostrar los empleados que sean distintos al departamento 10
select * from EMP where DEPT_NO <> 10;
--select * from EMP where DEPT_NO != 10;
--operadores racionales
--permitenfiltrar por mas de una condicion, solamenye oodemos tener un where
--and: todas las condiciones se deben 
--or: Devuelve registros de cada condicion
--not: Negacion de una condicion
--Mostrar todos los empleados con oficio director y un salario mayor a 300.00
select * from EMP where OFICIO ='DIRECTOR'
and SALARIO > 300000;
--MOSTRAR TODOS LOS EMPLEADOS QUE SENA DEL DEPARTAMENTO 10 Y DEL DPTO.20
select * from EMP where DEPT_NO=10 or DEPT_NO=20;
--Mostrar los empleados que no sena del dept. 20
select * from EMP where NOT DEPT_NO=20;--NEGACION NUNCA
select * from EMP where DEPT_NO<>20;
--Existen otra serie de operadores de comparacion ademas de los basicos
--Betwen busca esntre dos rangos inclusive
--mostrar todos los empleados que tengan un salario entre 123500 y 318500
select * from EMP where SALARIO between 123500 and 318500;
select * from EMP where SALARIO >=123500 and SALARIO <=318500;
--Operador IN permite buscar entre diferentes valores  de un mismo campo
--Mostar todos los empleados del departamento 10 y 20 y del 30, 40, 50, 66, 88
select * from EMP where DEPT_NO in (10, 20, 30, 40, 50, 66, 88);
--operador NOT IN que busca entre diferentes valores de un mismo campo y 
--devuelve los que no correspondan
--Mostrar todos los empleados que no esten en el departamento 10 y 20
select * from EMP where NOT DEPT_NO in (10, 20);--esto es un anegacion no eficiente
select * from EMP where DEPT_NO not in (10, 20);--esto es un operador
--Tenemos un operador que nos permite hacer busquedas dentro de textos
--es el operador like y utilioza caracteres especiales para las busquedas:
  --? busca sie el caracter es un numero
  --_ Cualquier unico caracter
  --% cualquier caracter y cualquier tamaño
--Mostrar todos los emoleadis cuyo apelliso comienza por s
select * from EMP where APELLIDO like 's%';
-- Mostrar todos los empleados que comienzan por s y acaban en a
select * from EMP where APELLIDO like 's%a';
--Mostrar todos los empleados cuyo apellido tenga 4 letras
select * from EMP where APELLIDO like '____';
select * from EMP where APELLIDO like '_a%';
--Clausula distinct elimina datos repetidos de la consulta
--se suele utilizar con pocos campos
select distinct OFICIO from EMP;
--campos calculados , son columnas que no existen en la tabla
--y que podemos generar con una consulta
--los campos calculados siempre deben tener un ALIAS
select APELLIDO, OFICIO, SALARIO + COMISION as TOTAL_SALARIO from EMP;
 
  