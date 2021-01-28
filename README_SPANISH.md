# Prueba de backend de Cornershop

Esta prueba técnica requiere el diseño e implementación (usando Django) de un sistema de gestión para coordinar la entrega de comida a los empleados de Cornershop.

## Después de terminar tu prueba, comparte este repositorio con: @ Cornershop-hr @Alecornershop @roherrera @ stichy23

Si tiene alguna pregunta técnica, comuníquese con osvaldo@cornershopapp.com
Título del proyecto: Backend-Test- (Apellido)

## Descripción

El proceso actual consiste en que una persona (Nora) envíe un mensaje de texto vía Whatsapp a todos los empleados chilenos, el mensaje contiene el menú de hoy con las diferentes alternativas para el almuerzo.

> ¡Hola!
> Comparto con ustedes el menú de hoy :)
>
> Opción 1: Pastel de maíz, Ensalada y Postre
> Opción 2: Arroz con pepitas de pollo, ensalada y postre
> Opción 3: Arroz con hamburguesa, Ensalada y Postre
> Opción 4: Ensalada y Postre de Pollo Premium.
>
> ¡Que tengas un buen día!

Con el nuevo sistema, Nora debería poder:

- Crea un menú para una fecha específica.
- Enviar un recordatorio de Slack con el menú de hoy a todos los empleados chilenos (este proceso debe ser asincrónico).

Los empleados deben poder:

- Elija su comida preferida (hasta las 11 AM CLT).
- Especificar personalizaciones (por ejemplo, sin tomates en la ensalada).

Nora debería ser el único usuario que pueda ver lo que los empleados de Cornershop han solicitado y crear y editar el menú de hoy. Los empleados deberían poder especificar qué quieren para el almuerzo, pero no deberían poder ver lo que otros han solicitado.

NOTA: Los recordatorios de holgura deben contener una URL al menú de hoy con el siguiente patrón https://nora.cornershop.io/menu/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx (un UUID), esta página no debe requerir la autenticación de ningún tipo.

## Aspectos a evaluar

Dado que el sistema es muy simple (pero poderoso en términos de yumminess) evaluaremos estos aspectos:

- funcionalidad
- Prueba
- documentación
- Diseño de software
- Estilo de programación
- Uso adecuado del marco

## Aspectos a ignorar

- Diseño visual de la solución
- Despliegue de la solución

## Restricciones

- Está prohibido el uso del administrador de Django.