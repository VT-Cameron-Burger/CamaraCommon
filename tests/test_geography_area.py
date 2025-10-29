"""
Tests for geography and area data types.
"""

import pytest
from CamaraCommon.Geography import (
    Latitude,
    Longitude,
    Point,
    PointList,
    AreaType,
    Area,
    Circle,
    Polygon,
)


class TestGeographyTypes:
    """Test geography data types."""

    def test_valid_latitude(self):
        """Test valid latitude values."""
        valid_latitudes = [-90.0, -45.5, 0.0, 45.5, 90.0, 50.735851]

        for lat_value in valid_latitudes:
            lat = Latitude(value=lat_value)
            assert lat.value == lat_value

    def test_invalid_latitude(self):
        """Test invalid latitude values."""
        invalid_latitudes = [-90.1, -100.0, 90.1, 100.0, 180.0]

        for lat_value in invalid_latitudes:
            with pytest.raises(ValueError):
                Latitude(value=lat_value)

    def test_valid_longitude(self):
        """Test valid longitude values."""
        valid_longitudes = [-180.0, -90.5, 0.0, 90.5, 180.0, 7.10066]

        for lon_value in valid_longitudes:
            lon = Longitude(value=lon_value)
            assert lon.value == lon_value

    def test_invalid_longitude(self):
        """Test invalid longitude values."""
        invalid_longitudes = [-180.1, -200.0, 180.1, 200.0, 360.0]

        for lon_value in invalid_longitudes:
            with pytest.raises(ValueError):
                Longitude(value=lon_value)

    def test_valid_point(self):
        """Test valid Point creation."""
        lat = Latitude(value=50.735851)
        lon = Longitude(value=7.10066)
        point = Point(latitude=lat, longitude=lon)

        assert point.latitude.value == 50.735851
        assert point.longitude.value == 7.10066

    def test_point_list_valid_range(self):
        """Test PointList with valid number of points."""
        points = [
            Point(
                latitude=Latitude(value=50.735851), longitude=Longitude(value=7.10066)
            ),
            Point(
                latitude=Latitude(value=50.736851), longitude=Longitude(value=7.11066)
            ),
            Point(
                latitude=Latitude(value=50.737851), longitude=Longitude(value=7.10566)
            ),
        ]
        point_list = PointList(points=points)
        assert len(point_list) == 3
        assert point_list[0].latitude.value == 50.735851

    def test_point_list_too_few_points(self):
        """Test PointList with too few points."""
        points = [
            Point(
                latitude=Latitude(value=50.735851), longitude=Longitude(value=7.10066)
            ),
            Point(
                latitude=Latitude(value=50.736851), longitude=Longitude(value=7.11066)
            ),
        ]
        with pytest.raises(ValueError, match="PointList must have at least 3 points"):
            PointList(points=points)

    def test_point_list_too_many_points(self):
        """Test PointList with too many points."""
        points = []
        for i in range(16):  # More than max 15
            points.append(
                Point(
                    latitude=Latitude(value=50.0 + i * 0.001),
                    longitude=Longitude(value=7.0 + i * 0.001),
                )
            )
        with pytest.raises(ValueError, match="PointList must have at most 15 points"):
            PointList(points=points)


class TestAreaTypes:
    """Test area data types."""

    def test_area_type_enum(self):
        """Test AreaType enum values."""
        assert AreaType.CIRCLE == "CIRCLE"
        assert AreaType.POLYGON == "POLYGON"

    def test_valid_circle(self):
        """Test valid Circle creation."""
        center = Point(
            latitude=Latitude(value=50.735851), longitude=Longitude(value=7.10066)
        )
        circle = Circle(center=center, radius=1000.0)

        assert circle.center.latitude.value == 50.735851
        assert circle.center.longitude.value == 7.10066
        assert circle.radius == 1000.0

    def test_circle_with_different_radii(self):
        """Test Circle with different radius values."""
        center = Point(latitude=Latitude(value=0.0), longitude=Longitude(value=0.0))

        # Test small radius
        small_circle = Circle(center=center, radius=100.0)
        assert small_circle.radius == 100.0

        # Test large radius
        large_circle = Circle(center=center, radius=50000.0)
        assert large_circle.radius == 50000.0

    def test_valid_polygon(self):
        """Test valid Polygon creation."""
        points = [
            Point(
                latitude=Latitude(value=50.735851), longitude=Longitude(value=7.10066)
            ),
            Point(
                latitude=Latitude(value=50.736851), longitude=Longitude(value=7.11066)
            ),
            Point(
                latitude=Latitude(value=50.737851), longitude=Longitude(value=7.10566)
            ),
        ]
        point_list = PointList(points=points)
        polygon = Polygon(boundary=point_list)

        assert len(polygon.boundary) == 3
        assert polygon.boundary.points[0].latitude.value == 50.735851

    def test_area_with_circle(self):
        """Test Circle as an Area type."""
        center = Point(
            latitude=Latitude(value=50.735851), longitude=Longitude(value=7.10066)
        )
        circle = Circle(center=center, radius=1000.0)

        assert circle.areaType == AreaType.CIRCLE
        assert circle.center.latitude.value == 50.735851
        assert circle.radius == 1000.0

    def test_area_with_polygon(self):
        """Test Polygon as an Area type."""
        points = [
            Point(
                latitude=Latitude(value=50.735851), longitude=Longitude(value=7.10066)
            ),
            Point(
                latitude=Latitude(value=50.736851), longitude=Longitude(value=7.11066)
            ),
            Point(
                latitude=Latitude(value=50.737851), longitude=Longitude(value=7.10566)
            ),
        ]
        point_list = PointList(points=points)
        polygon = Polygon(boundary=point_list)

        assert polygon.areaType == AreaType.POLYGON
        assert len(polygon.boundary) == 3
        assert polygon.boundary.points[0].latitude.value == 50.735851
