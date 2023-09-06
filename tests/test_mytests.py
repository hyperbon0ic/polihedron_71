from pytest import approx
from common.r3 import R3
from shadow.polyedr import Facet, Polyedr
from math import sqrt, pi


class TestR3():

    def test_length_1(self):
        assert R3(1, 1, 1).length() == sqrt(3)

    def test_area_1(self):
        assert R3.area_2d(R3(0, 0, 0), R3(0, 3, 0), R3(3, 0, 0)) == approx(4.5)


class TestFacet():

    def test_angle_1(self):
        f = Facet([R3(0.0, 0.0, 0.0), R3(3.0, 0.0, 0.0), R3(0.0, 3.0, 0.0)])
        assert f.angle() == approx(0)

    def test_angle_2(self):
        f = Facet([R3(0, 0, 0), R3(0, 4, 0), R3(0, 0, 5)])
        assert f.angle() == approx(pi/2)

    def test_angle_3(self):
        f = Facet([R3(0, 0, 0), R3(3, 0, 0), R3(3, 3, 3)])
        assert f.angle() == approx(pi/4)

    def test_angle_4(self):
        f = Facet([R3(0, 0, 0), R3(-3, 0, 0), R3(-3, -3, -3)])
        assert f.angle() == approx(pi/4)

    def test_is_angle_less_1(self):
        f = Facet([R3(0.0, 0.0, 0.0), R3(3.0, 0.0, 0.0), R3(0.0, 3.0, 0.0)])
        assert f.is_angle_less() is True

    def test_is_angle_less_2(self):
        f = Facet([R3(0, 0, 0), R3(0, 4, 0), R3(0, 0, 5)])
        assert f.is_angle_less() is False

    def test_is_angle_less_3(self):
        f = Facet([R3(0, 0, 0), R3(3, 0, 0), R3(3, 3, 3)])
        assert f.is_angle_less() is False

    def test_is_angle_less_4(self):
        f = Facet([R3(0, 0, 0), R3(-3, 0, 0), R3(-3, -3, -3)])
        assert f.is_angle_less() is False

    def test_is_center_in_1(self):
        f = Facet([R3(0, 0, 0), R3(3, 0, 0), R3(3, 3, 0)])
        assert f.is_center_in(1) is False

    def test_is_center_in_2(self):
        f = Facet([R3(0, 0, 0), R3(1, 0, 0), R3(1, 1, 0)])
        assert f.is_center_in(1) is True

    def test_is_center_in_3(self):
        f = Facet([R3(0, 0, 20), R3(1, 0, 10), R3(1, 10, 10)])
        assert f.is_center_in(1) is True


class TestPolyedr():

    def test_area_1(self):
        assert Polyedr(f"data/test1.geom").area() == approx(6)

    def test_area_2(self):
        assert Polyedr(f"data/test2.geom").area() == approx(0)

    def test_area_3(self):
        assert Polyedr(f"data/test3.geom").area() == approx(3)

    def test_area_4(self):
        assert Polyedr(f"data/test4.geom").area() == approx(0)

    def test_area_5(self):
        assert Polyedr(f"data/test5.geom").area() == approx(3)

# python3 -B -m pytest -p no:cacheprovider tests/test_mytests.py
