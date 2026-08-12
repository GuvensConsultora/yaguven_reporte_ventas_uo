# Reporte de Ventas por Unidad Operativa (Yagüven)

Exporta a Excel la venta facturada separando **contado** de **cuenta corriente**, con corte
por Unidad Operativa (sucursal) y por fecha, en pesos y en cantidad de tickets.

## Cómo se usa

1. **Contabilidad → Configuración → Condiciones de Pago: Ventas de Contado** — tildar cuáles
   condiciones corresponden a ventas de contado. No viene ninguna marcada: el criterio lo
   define el usuario.
2. **Contabilidad → Informes → Ventas por Unidad Operativa** — elegir el rango y exportar.

## Criterio

La separación es por la **condición de pago** del comprobante, no por el medio con que se
cobró: una venta de contado pagada con tarjeta sigue siendo de contado.

Los comprobantes sin condición de pago cargada no se adivinan: van en su propia columna,
con su detalle en una solapa aparte.

## Detalles de implementación

- Las **notas de crédito no heredan** la condición de pago de la factura que revierten, así
  que se resuelven por `reversed_entry_id`. Sin eso cada NC restaría del grupo equivocado.
- Los **tickets se cuentan sólo sobre las facturas**; las NC restan del importe pero no son
  un ticket generado. Cada ticket de POS emite su factura, así que queda incluido una sola vez.
- `account_journal.name` es traducible y se guarda como JSONB: se extrae con `->>` y se cae a
  `en_US`. Un `COALESCE(aj.name, '')` directo falla con *invalid input syntax for type json*.

## Dependencias

`account` · `yaguven_operating_unit` · python `xlsxwriter`
