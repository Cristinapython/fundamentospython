select * from EMP;
select APELLIDO, OFICIO, SALARIO * 14 as ANUAL
from EMP WHERE
 COMISION > 100000; 
select APELLIDO, OFICIO, SALARIO * 14 as ANUAL
from EMP WHERE
 SALARIO * 14 > 750000;
 select APELLIDO, OFICIO, SALARIO * 14 as ANUAL
from EMP WHERE
SALARIO * 14 + COMISION > 1000000;
select * from EMP order by DEPT_NO DESC, OFICIO; 
select * from ENFERMO where FECHA_NAC < '1/1/70';
select * from ENFERMO where FECHA_NAC < '1/1/70'
order by INSCRIPCION;
select * from PLANTILLA:
-------pendiente acabar------
--Mostrar el nº empleados de la tabla
select count(*) as REGISTROS from EMP;
--PODEMOS COMBINAR VARIAS FUNCIONES EN UNA MISMA CONSULTA
--MOSTRAR NUMERO DE EMPLEADOS Y LASUMA SALARIAL DE TODOS
select count(*) as registros, sum(salario) as SUMASALARIAL from EMP;
--Queremos saber el numero de empleados por cada oficio
select count(*) as EMPLEADOS, OFICIO from EMP
group by OFICIO;
--Mostrar el maximo salario , numero de personas 
--por cadad oficio y por cada departamento
select max(SALARIO) as MAXIMOSALARIO,
count(*) as PERSONAS, OFICIO, DEPT_NO
from EMP
group by OFICIO, DEPT_NO;
--Mostrar el numero de personas por cada oficio
--pero solamente mostrando DIRECTOR Y ANALISTA
select count(*) as PERSONAS, OFICIO
from EMP
where OFICIO IN ('ANALISTA', 'DIRECTOR')
group by OFICIO;
--Mostrar el numero dee empleados por cada oficio 
--pero solamente mostrando los oficios donde tengamos + de 2 personas trabajando
select count(*) as PERSONAS, OFICIO
from EMP
group by OFICIO
having count(*) > 2;
--combinadas
--Mostrar la suma salarial por cada oficio
--solamente de las personmas qie tengan una comision
--mayor a cero
select sum(SALARIO) as SUMASALARIAL, OFICIO
from EMP
where COMISION > 0
group by OFICIO;
--Mostrar la suma salarial por cada oficio
--solamente de las personmas qie tengan una comision
--mayor a cero Y CUYA SUMA salarial sea mayor a 51500
select sum(SALARIO) as SUMASALARIAL, OFICIO
from EMP
where COMISION > 0
group by OFICIO
having sum(SALARIO) > 515000;
--ejercicio 1 CONSULTAS DE AGRUPACION
--Encontrar el salario medio de los analistas, mostrando el número de los empleados con oficio analista.
select AVG(SALARIO) as MEDIA, COUNT(*) as PERSONAS, OFICIO
from EMP
where OFICIO = 'ANALISTA'
group by OFICIO;
--Encontrar el salario más alto, mas bajo y la diferencia entre ambos de todos los empleados con oficio EMPLEADO.
select OFICIO, MAX(SALARIO) as SALARIOMAX
, MIN(SALARIO) as SALARIOMIN
, MAX(SALARIO) - MIN(SALARIO) as DIFERENCIA
from EMP
group by OFICIO
having OFICIO = 'EMPLEADO';
--Visualizar los salarios mayores para cada oficio.
select OFICIO, MAX(SALARIO)
from EMP
group by OFICIO;
--Visualizar el número de personas que realizan cada oficio en cada departamento.
select DEPT_NO, count(*) as PERSONAS, OFICIO
from EMP
group by DEPT_NO, OFICIO
order by 1;
--Buscar aquellos departamentos con cuatro o más personas trabajando.
select count(*) as PERSONAS, DEPT_NO
from EMP
group by DEPT_NO
having count(*) >= 4;
--7.Visualizar el número de enfermeros, enfermeras e 
--interinos que hay en la plantilla, ordenados por la función
select count(*) as PERSONAS, FUNCION 
from PLANTILLA
where FUNCION IN ('ITERINO', 'ENFERMERO', 'ENFERMERA')
group by FUNCION;
--8.Visualizar departamentos, oficios y número de personas,
-- para aquellos departamentos que tengan dos o más personas trabajando en el mismo oficio.
select count(*) as PERSONAS, OFICIO, DEPT_NO
from EMP
group by OFICIO, DEPT_NO
having count(*)>=2;
--10.Calcular el salario medio de la plantilla de la sala 6, 
--según la función que realizan. Indicar la función y el número de empleados.
SELECT AVG(SALARIO) AS MEDIA SALARIAL, FUNCION
, count(*) as EMPLEADOS
from PLANTILLA
whwew SALA_COD = 6
group by FUNCION;
select * from PLANTILLA;
--12.Averiguar los últimos empleados que se dieron de alta en
-- la empresa en cada uno de los oficios, ordenados por la fecha.
select max(FECHA_ALT) as MAXFECHAALAT, OFICIO
from EMP
group by OFICIO
order by MAXFECHAALAT desc;

--13.Mostrar el número de hombres y 
--el número de mujeres que hay entre los enfermos.
select count(*) as ENFERMERAS, SALA_COD
from PLANTILLA
where FUNCION = 'ENFERMERA'
group by SALA_COD;
--Tenemos una tabla de empleados 
select * from DEPT;
select TABLA1.CAMPO1, TABLA1, CAMPO2
--Mostrar el apellido, oficio, nombre de dpto. y localidad
--de los empleados
select EMP.APELLIDO, EMP.OFICIO
, DEPT.DNOMBRE, DEPT.LOC
from EMP
inner join DEPT
on EMP.DEPT_NO = DEPT.DEPT_NO;
--MOSTRAR EL APELLIDO , OFICIO, NOMBRE DEPARTAMENTO Y LOCALIDAD DE 
--LOS EMPLEADOS DE SEVILLA
select EMP.APELLIDO, EMP.OFICIO
, DEPT.DNOMBRE, DEPT.LOC
from EMP
INNER JOIN DEPT
on EMP.DEPT_NO = DEPT.DEPT_NO
where DEPT.LOC = 'SEVILLA';
--alias en n ombre tabla
select e.apellido, e.oficio
, d.NOMBRE







