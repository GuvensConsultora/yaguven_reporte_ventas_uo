# -*- coding: utf-8 -*-
{
    "name": "Reporte de Ventas por Unidad Operativa (Yagüven)",
    "summary": "Ventas de contado y cuenta corriente por sucursal y por fecha, "
               "en $ y en cantidad de tickets.",
    "description": """
Exporta a Excel la venta facturada separando **contado** de **cuenta corriente**, con
corte por Unidad Operativa (sucursal) y por fecha.

- La separación es por la CONDICIÓN DE PAGO del comprobante, no por el medio con que se
  cobró: una venta de contado pagada con tarjeta sigue siendo de contado. Cuáles
  condiciones son de contado lo define el usuario desde la UI, no está fijado en código.
- Los comprobantes sin condición de pago cargada no se adivinan: van en su propia
  columna y con su detalle, para que el usuario decida.
- Las notas de crédito no heredan la condición de pago de la factura que revierten, así
  que se resuelven por el comprobante original. Sin eso cada NC restaría del grupo
  equivocado.
- Los tickets se cuentan sólo sobre las facturas; las NC restan del importe pero no son
  un ticket generado. Cada ticket de POS emite su factura, así que queda incluido.
""",
    "version": "19.0.1.0.0",
    "category": "Accounting",
    "author": "Yagüven C.G.",
    "license": "LGPL-3",
    "depends": [
        "account",
        "yaguven_operating_unit",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/account_payment_term_views.xml",
        "wizard/reporte_ventas_uo_wizard_views.xml",
    ],
    "external_dependencies": {"python": ["xlsxwriter"]},
    "installable": True,
    "application": False,
}
