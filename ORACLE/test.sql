select * from DEPT where DEPT_NO=10;
select APELLIDO, DIRECCION from ENFERMO where INSCRIPCION= 59076;
select * from PLANTILLA;
select APELLIDO, FUNCION from PLANTILLA where TURNO=
delete from ENFERMO where INSCRIPCION=1;
rollback;
commit;
--si no le decimos commit o rollback no se ejecuta
insert into DEPT values(88, 'NUEVO', 'NUEVO')
