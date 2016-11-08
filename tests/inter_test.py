from datetime import datetime, timedelta

from intervals_inter.inter import intersection


def test_intersections_int():
    values = (
        (10, 20), (19, 40),
        (15, 31), (14, 25),
        (5, 14), (10, 15))
    interval = (15, 35)
    res = intersection(values, interval)
    assert res is not None
    assert res.max_intersects == 4
    assert res.timestamp == 19


def test_intersections_datetime():
    some_time = datetime.now()
    values = (
        (some_time + timedelta(minutes=10), some_time + timedelta(minutes=20)),
        (some_time + timedelta(minutes=19), some_time + timedelta(minutes=40)),
        (some_time + timedelta(minutes=15), some_time + timedelta(minutes=31)),
        (some_time + timedelta(minutes=14), some_time + timedelta(minutes=25)),
        (some_time + timedelta(minutes=5), some_time + timedelta(minutes=14)),
        (some_time + timedelta(minutes=10), some_time + timedelta(minutes=15))
    )
    interval = (some_time + timedelta(minutes=15), some_time + timedelta(minutes=35))
    res = intersection(values, interval)
    assert res is not None
    assert res.max_intersects == 4
    assert res.timestamp == some_time + timedelta(minutes=19)