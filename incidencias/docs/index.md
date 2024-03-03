---
title: Sistemas de Gestión Empresarial
subtitle: Modulo Incidencias
layout: page
show_sidebar: false
hero_height: is-fullwidth
---
## Nombre Comercial: 
Incidencias Técnicas

## Nombre Técnico:
incidencias

## Descripción corta: 
Módulo permite crear contratos, gestionar las zonas de trabajo de cada trabajador, realizar incidencias, agendarlas y gestionarlas. Además permite el consumo de los materiales utilizados en la misma, permitiendo el seguimiento de su estado en cada momento. 

# Información detallada
## Funciones de CAC (Centro Atención al Cliente)
  - Ver todo tipo de incidencias independientemente de su estado.
   - Crear los contratos y asociarlos a clientes
   - Crear nueva incidencia:
      - Poner DNI del cliente afectado.
      - Poner fecha y hora que se ha pactado con el cliente para ir a hacer la reparación.
      - Indicar en el texto de la incidencia y marcar los servicios afectados.

## Funciones de Jefe Técnico:
   - Gestionar zonas de trabajo
   - Ver todo tipo de incidencias independientemente de su estado
   - Confirmar datos de las incidencias, modificar datos y pasarlas a otros estados:
      - Confirmar fecha y hora pactada con el cliente.
      - Cambiar estado a “En gestión”.
      - Introducir anotaciones.
      - Introducir texto de solución
      - Cambiar estado a “Solucionada”.

## Funciones de Técnicos:
   - Ver incidencias asignadas independientemente del estado en el que estén, pudiendo obtener información útil.
   - Gestionar incidencias mientras estén en estado “En gestión”:
      - Introducir anotaciones.
      - Introducir texto de solución.
   - Realizar consumo de materiales de las incidencias”.

## URL del repositorio:
   - [Link](https://github.com/JosemaVlc/modulo_incidencias).

## Dependencias de otros modulos:
   - base
   - contacts
      - res.partner
      - res.country
      - res.country.state
   - hr
      - hr.employee

## Dependencias externas:
   - Geopy
