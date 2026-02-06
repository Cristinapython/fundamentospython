-- Necsito ver kis datos dek empleado que mas cobra:
--1)necesitamos saber el máximo salario de la tabla de empleados
select max(SALARIO) from EMP;



--650000
--2)Realizamos la consulta para mostrar los datos del 
--empleado que mas cobra
select * from EMP where SALARIO=650000;
-------------

SELECT *FROM EMP WHERE SALARIO=
(SELECT MAX(SALARIO)FROM EMP);



--EL PROMEDIO DE LOS 4 SUELDOS SUPERIORES IGNORANDO AL PRESI
--AVG(SALARIO)
OFICIO<> 'PRESIDENTE';

--SALARIO > ??
-- LOS 4 SALARIOS
SELECT SALARIO FROM EMP ORDER BY SALARIO DESC;
--MEDIA SALARIAL DE LOS EMPLEADOS SIN EL PRESIDEENTE
SELECT AVG(SALARIO) as MEDIA_SALARIAL from EMP
where OFICIO <> 'PRESIDENTE';
SELECT * FROM EMP WHERE OFICIO <>'PRESIDENTE';
--NECESITAMOS LOS 4 PRIMEROS SALARIOS

SELECT avg(salario) as Media from EMP 
WHERE OFICIO <> 'PRESIDENTE' and rownum <= 4
ORDER BY SALARIO DESC;
SELECT * FROM EMP WHERE ROWNUM <=4;


--mostras todos los empeados que tengan el mismo oficio que 
--alonso y que cobren mas que sala (apellido)
SELECT* from emp;
--mostrr los empleados que tengan
--el mismo oficio que jimenez y alonso
--SUBCONSULTA
SELECT OFICIO FROM EMP WHERE APELLIDO='JIMENEZ'
OR APELLIDO='ALONSO';
---SUBCONSULTA
SELECT * FROM EMP WHEWE OFICIO IN
(SELECT OFICIO FROM EMP WHERE APELLIDO ='JIMENEZ' OR APELLIDO='ALONSO');










