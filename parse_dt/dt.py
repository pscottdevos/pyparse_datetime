import numbers
from datetime import datetime

import pytz
from dateutil.parser import parse
from iso8601 import parse_date, ParseError

__all__ = ['now', 'parse_datetime']


def now(tzinfo=None):
    """returns and aware datetime representing the current date and time
    in the timezone provided by tzinfo (or pytz.UTC if tzinfo is None)
    """
    tzinfo = tzinfo or pytz.utc
    return parse_datetime(datetime.utcnow(), tzinfo)


def parse_datetime(value, tzinfo=None):
    """returns an aware datetime in the timezone specified by tzinfo.
    If tzinfo is not supplied or is None, the resulting datetime will
    be in the pytz.UTC or iso8601.UTC timezone (as described below)

    if value is a string, it must be iso8601 compatible. If the offset is
    not specified the resulting aware datetime will use tzinfo if provided
    otherwise it will use iso8601.UTC

    if value is a naive datetime, it will be assumed to be in UTC and will
    then be converted to the timezone specified by tzinfo (if provided)

    if value is an aware datetime, it will be converted to an aware datetime
    in pytz.UTC or in tzinfo it if is provided.
    """
    if isinstance(value, str):
        if "T" not in value:
            if "/" in value:
                mm, dd, yy_time = value.split("/")
                yy, tt = yy_time.split(" ")
                value = f"{yy}-{mm}-{dd}T{tt}"
            else:
                value = "T".join(value.split())
        try:
            aware_dt = parse_date(value)
        except ParseError:
            aware_dt = pytz.utc.localize(parse(value))
    elif isinstance(value, numbers.Number):
        aware_dt = datetime.fromtimestamp(value, tz=tzinfo or pytz.utc)
    else:
        aware_dt = value if value.tzinfo else pytz.utc.localize(value)
    if tzinfo:
        return aware_dt.astimezone(tzinfo)
    return aware_dt.astimezone(pytz.utc)
