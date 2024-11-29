import pytest
from pathlib import Path
from homework.car.car import Car

class TestCarRoutes:
    """Tests for the Car class using route files."""
    @pytest.mark.parametrize(
        ("route_id", "destination"),
        [
            (5, (266, 72.0, -187.0)),
            (10, (89, -120.0, 4.0)),
            (20, (208, 1256.0, -804.0)),
            (50, (161, -2370.0, -783.0)),
            (100, (38, 1095.0, 1899.0)),
            (200, (68, -1656.0, -955.0)),
            (500, (34, -3594.0, -840.0)),
            (1000, (259, -91.0, 4303.0)),
        ],
    )
    def test_routes(self, route_id, destination):
        """Test the Car class with various routes."""
        car = Car()
        route_path = Path("homework", "car", "routes", f"{route_id}.txt")

        # Read and process the route
        route = route_path.read_text(encoding="utf-8")
        for s in route.split():
            car.process(s)

        # Check the result against the expected destination
        result = (car.direction, round(car.x, 0), round(car.y, 0))
        assert result == destination, f"Failed for route_id {route_id}: {result} != {destination}"

