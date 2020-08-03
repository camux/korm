from decimal import Decimal
import datetime


def encoder(rec):
    for k, v in rec.items():
        if type(v) is datetime.date or type(v) is datetime.datetime:
            rec[k] = v.isoformat()
        elif type(v) is Decimal:
            rec[k] = float(v)
    return rec
