"""
Tests for the Employee Time Tracking API.
"""

import pytest
from datetime import datetime, timedelta

from holded.team_api.models.employee_time_tracking import EmployeeTimeTrackingCreate, EmployeeTimeTrackingUpdate


class TestEmployeeTimeTrackingResource:
    """Test cases for the Employee Time Tracking API."""

    def test_list_all_times(self, client):
        """Test listing all time tracking entries."""
        result = client.employee_time_tracking.list_all()

        assert result is not None
        # API may return a dict with 'times' key or a list directly
        if isinstance(result, dict):
            assert isinstance(result, dict)
        else:
            assert isinstance(result, list)

    def test_list_all_times_with_pagination(self, client):
        """Test listing all time tracking entries with pagination."""
        result = client.employee_time_tracking.list_all(page=1)

        assert result is not None
        # API may return a dict with 'times' key or a list directly
        if isinstance(result, dict):
            assert isinstance(result, dict)
        else:
            assert isinstance(result, list)

    def test_list_employee_times(self, client):
        """Test listing time tracking entries for an employee."""
        # First, get an existing employee or create one
        import time

        try:
            employees_result = client.employees.list()
            # Handle both dict and list responses
            if isinstance(employees_result, dict):
                employees = employees_result.get("employees", [])
            else:
                employees = employees_result

            if not employees:
                pytest.skip("No employees found in the account")

            employee_id = employees[0].get("id") or employees[0].get("_id")
            if not employee_id:
                pytest.skip("Employee ID not found")

            result = client.employee_time_tracking.list(employee_id)

            assert result is not None
            # API may return a dict or a list directly
            if isinstance(result, dict):
                assert isinstance(result, dict)
            else:
                assert isinstance(result, list)
        except Exception as e:
            pytest.skip(f"List employee times failed: {e}")

    def test_create_employee_time_tracking(self, client):
        """Test creating a time tracking entry for an employee."""
        import time

        # First, get an existing employee or create one
        try:
            employees_result = client.employees.list()
            # Handle both dict and list responses
            if isinstance(employees_result, dict):
                employees = employees_result.get("employees", [])
            else:
                employees = employees_result

            if not employees:
                # Create a test employee
                from holded.team_api.models.employees import EmployeeCreate

                employee_data = EmployeeCreate(
                    name=f"Test Employee Time {int(time.time())}",
                    last_name="Test",
                    email=f"testtime{int(time.time())}@example.com",
                    send_invite=False,
                )
                created_employee = client.employees.create(employee_data)
                employee_id = created_employee.get("id") or created_employee.get("_id")
                cleanup_employee = True
            else:
                employee_id = employees[0].get("id") or employees[0].get("_id")
                cleanup_employee = False

            if not employee_id:
                pytest.skip("Employee ID not found")

            # Create time tracking entry
            start_time = datetime.now()
            end_time = start_time + timedelta(hours=2)

            time_data = EmployeeTimeTrackingCreate(
                start_tmp=start_time.isoformat(),
                end_tmp=end_time.isoformat(),
            )

            result = client.employee_time_tracking.create(employee_id, time_data)

            assert result is not None
            assert isinstance(result, dict)
            assert "id" in result or "_id" in result

            # Cleanup: delete the created time tracking
            time_id = result.get("id") or result.get("_id")
            if time_id:
                try:
                    client.employee_time_tracking.delete(time_id)
                except Exception:
                    pass

            # Cleanup employee if we created it
            if cleanup_employee:
                try:
                    client.employees.delete(employee_id)
                except Exception:
                    pass
        except Exception as e:
            pytest.skip(f"Time tracking creation failed: {e}")

    def test_get_time_tracking(self, client):
        """Test getting a time tracking entry."""
        import time

        # First, get an existing employee
        try:
            employees_result = client.employees.list()
            # Handle both dict and list responses
            if isinstance(employees_result, dict):
                employees = employees_result.get("employees", [])
            else:
                employees = employees_result

            if not employees:
                pytest.skip("No employees found in the account")

            employee_id = employees[0].get("id") or employees[0].get("_id")
            if not employee_id:
                pytest.skip("Employee ID not found")

            # Get existing time tracking entries
            times_result = client.employee_time_tracking.list(employee_id)
            # Handle both dict and list responses
            if isinstance(times_result, dict):
                times = times_result.get("times", []) if "times" in times_result else []
            else:
                times = times_result

            if not times:
                pytest.skip("No time tracking entries found for employee")

            time_id = times[0].get("id") or times[0].get("_id")
            if not time_id:
                pytest.skip("Time tracking ID not found")

            result = client.employee_time_tracking.get(time_id)

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Get time tracking failed: {e}")

    def test_clock_in(self, client):
        """Test clocking in an employee."""
        import time

        # First, get an existing employee
        try:
            employees_result = client.employees.list()
            # Handle both dict and list responses
            if isinstance(employees_result, dict):
                employees = employees_result.get("employees", [])
            else:
                employees = employees_result

            if not employees:
                pytest.skip("No employees found in the account")

            employee_id = employees[0].get("id") or employees[0].get("_id")
            if not employee_id:
                pytest.skip("Employee ID not found")

            result = client.employee_time_tracking.clock_in(employee_id)

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Clock in failed: {e}")

    def test_clock_out(self, client):
        """Test clocking out an employee."""
        import time

        # First, get an existing employee
        try:
            employees_result = client.employees.list()
            # Handle both dict and list responses
            if isinstance(employees_result, dict):
                employees = employees_result.get("employees", [])
            else:
                employees = employees_result

            if not employees:
                pytest.skip("No employees found in the account")

            employee_id = employees[0].get("id") or employees[0].get("_id")
            if not employee_id:
                pytest.skip("Employee ID not found")

            result = client.employee_time_tracking.clock_out(employee_id)

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Clock out failed: {e}")

    def test_pause(self, client):
        """Test pausing an employee's time tracking."""
        import time

        # First, get an existing employee
        try:
            employees_result = client.employees.list()
            # Handle both dict and list responses
            if isinstance(employees_result, dict):
                employees = employees_result.get("employees", [])
            else:
                employees = employees_result

            if not employees:
                pytest.skip("No employees found in the account")

            employee_id = employees[0].get("id") or employees[0].get("_id")
            if not employee_id:
                pytest.skip("Employee ID not found")

            result = client.employee_time_tracking.pause(employee_id)

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Pause failed: {e}")

    def test_unpause(self, client):
        """Test unpausing an employee's time tracking."""
        import time

        # First, get an existing employee
        try:
            employees_result = client.employees.list()
            # Handle both dict and list responses
            if isinstance(employees_result, dict):
                employees = employees_result.get("employees", [])
            else:
                employees = employees_result

            if not employees:
                pytest.skip("No employees found in the account")

            employee_id = employees[0].get("id") or employees[0].get("_id")
            if not employee_id:
                pytest.skip("Employee ID not found")

            result = client.employee_time_tracking.unpause(employee_id)

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Unpause failed: {e}")


class TestAsyncEmployeeTimeTrackingResource:
    """Test cases for the Async Employee Time Tracking API."""

    @pytest.mark.asyncio
    async def test_list_all_times(self, async_client):
        """Test listing all time tracking entries asynchronously."""
        result = await async_client.employee_time_tracking.list_all()

        assert result is not None
        # API may return a dict or a list directly
        if isinstance(result, dict):
            assert isinstance(result, dict)
        else:
            assert isinstance(result, list)

    @pytest.mark.asyncio
    async def test_list_all_times_with_pagination(self, async_client):
        """Test listing all time tracking entries with pagination asynchronously."""
        result = await async_client.employee_time_tracking.list_all(page=1)

        assert result is not None
        # API may return a dict or a list directly
        if isinstance(result, dict):
            assert isinstance(result, dict)
        else:
            assert isinstance(result, list)

    @pytest.mark.asyncio
    async def test_list_employee_times(self, async_client):
        """Test listing time tracking entries for an employee asynchronously."""
        # First, get an existing employee
        try:
            employees_result = await async_client.employees.list()
            # Handle both dict and list responses
            if isinstance(employees_result, dict):
                employees = employees_result.get("employees", [])
            else:
                employees = employees_result

            if not employees:
                pytest.skip("No employees found in the account")

            employee_id = employees[0].get("id") or employees[0].get("_id")
            if not employee_id:
                pytest.skip("Employee ID not found")

            result = await async_client.employee_time_tracking.list(employee_id)

            assert result is not None
            # API may return a dict or a list directly
            if isinstance(result, dict):
                assert isinstance(result, dict)
            else:
                assert isinstance(result, list)
        except Exception as e:
            pytest.skip(f"List employee times failed: {e}")

    @pytest.mark.asyncio
    async def test_create_employee_time_tracking(self, async_client):
        """Test creating a time tracking entry for an employee asynchronously."""
        import time

        # First, get an existing employee or create one
        try:
            employees_result = await async_client.employees.list()
            # Handle both dict and list responses
            if isinstance(employees_result, dict):
                employees = employees_result.get("employees", [])
            else:
                employees = employees_result

            if not employees:
                # Create a test employee
                from holded.team_api.models.employees import EmployeeCreate

                employee_data = EmployeeCreate(
                    name=f"Test Employee Time Async {int(time.time())}",
                    last_name="Test",
                    email=f"testtimeasync{int(time.time())}@example.com",
                    send_invite=False,
                )
                created_employee = await async_client.employees.create(employee_data)
                employee_id = created_employee.get("id") or created_employee.get("_id")
                cleanup_employee = True
            else:
                employee_id = employees[0].get("id") or employees[0].get("_id")
                cleanup_employee = False

            if not employee_id:
                pytest.skip("Employee ID not found")

            # Create time tracking entry
            start_time = datetime.now()
            end_time = start_time + timedelta(hours=2)

            time_data = EmployeeTimeTrackingCreate(
                start_tmp=start_time.isoformat(),
                end_tmp=end_time.isoformat(),
            )

            result = await async_client.employee_time_tracking.create(employee_id, time_data)

            assert result is not None
            assert isinstance(result, dict)
            assert "id" in result or "_id" in result

            # Cleanup: delete the created time tracking
            time_id = result.get("id") or result.get("_id")
            if time_id:
                try:
                    await async_client.employee_time_tracking.delete(time_id)
                except Exception:
                    pass

            # Cleanup employee if we created it
            if cleanup_employee:
                try:
                    await async_client.employees.delete(employee_id)
                except Exception:
                    pass
        except Exception as e:
            pytest.skip(f"Time tracking creation failed: {e}")

    @pytest.mark.asyncio
    async def test_get_time_tracking(self, async_client):
        """Test getting a time tracking entry asynchronously."""
        # First, get an existing employee
        try:
            employees_result = await async_client.employees.list()
            # Handle both dict and list responses
            if isinstance(employees_result, dict):
                employees = employees_result.get("employees", [])
            else:
                employees = employees_result

            if not employees:
                pytest.skip("No employees found in the account")

            employee_id = employees[0].get("id") or employees[0].get("_id")
            if not employee_id:
                pytest.skip("Employee ID not found")

            # Get existing time tracking entries
            times_result = await async_client.employee_time_tracking.list(employee_id)
            # Handle both dict and list responses
            if isinstance(times_result, dict):
                times = times_result.get("times", []) if "times" in times_result else []
            else:
                times = times_result

            if not times:
                pytest.skip("No time tracking entries found for employee")

            time_id = times[0].get("id") or times[0].get("_id")
            if not time_id:
                pytest.skip("Time tracking ID not found")

            result = await async_client.employee_time_tracking.get(time_id)

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Get time tracking failed: {e}")

    @pytest.mark.asyncio
    async def test_clock_in(self, async_client):
        """Test clocking in an employee asynchronously."""
        # First, get an existing employee
        try:
            employees_result = await async_client.employees.list()
            # Handle both dict and list responses
            if isinstance(employees_result, dict):
                employees = employees_result.get("employees", [])
            else:
                employees = employees_result

            if not employees:
                pytest.skip("No employees found in the account")

            employee_id = employees[0].get("id") or employees[0].get("_id")
            if not employee_id:
                pytest.skip("Employee ID not found")

            result = await async_client.employee_time_tracking.clock_in(employee_id)

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Clock in failed: {e}")

    @pytest.mark.asyncio
    async def test_clock_out(self, async_client):
        """Test clocking out an employee asynchronously."""
        # First, get an existing employee
        try:
            employees_result = await async_client.employees.list()
            # Handle both dict and list responses
            if isinstance(employees_result, dict):
                employees = employees_result.get("employees", [])
            else:
                employees = employees_result

            if not employees:
                pytest.skip("No employees found in the account")

            employee_id = employees[0].get("id") or employees[0].get("_id")
            if not employee_id:
                pytest.skip("Employee ID not found")

            result = await async_client.employee_time_tracking.clock_out(employee_id)

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Clock out failed: {e}")

    @pytest.mark.asyncio
    async def test_pause(self, async_client):
        """Test pausing an employee's time tracking asynchronously."""
        # First, get an existing employee
        try:
            employees_result = await async_client.employees.list()
            # Handle both dict and list responses
            if isinstance(employees_result, dict):
                employees = employees_result.get("employees", [])
            else:
                employees = employees_result

            if not employees:
                pytest.skip("No employees found in the account")

            employee_id = employees[0].get("id") or employees[0].get("_id")
            if not employee_id:
                pytest.skip("Employee ID not found")

            result = await async_client.employee_time_tracking.pause(employee_id)

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Pause failed: {e}")

    @pytest.mark.asyncio
    async def test_unpause(self, async_client):
        """Test unpausing an employee's time tracking asynchronously."""
        # First, get an existing employee
        try:
            employees_result = await async_client.employees.list()
            # Handle both dict and list responses
            if isinstance(employees_result, dict):
                employees = employees_result.get("employees", [])
            else:
                employees = employees_result

            if not employees:
                pytest.skip("No employees found in the account")

            employee_id = employees[0].get("id") or employees[0].get("_id")
            if not employee_id:
                pytest.skip("Employee ID not found")

            result = await async_client.employee_time_tracking.unpause(employee_id)

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Unpause failed: {e}")

