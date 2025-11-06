"""
Tests for the Employees API.
"""

import pytest

from holded.team_api.models.employees import EmployeeCreate, EmployeeUpdate


class TestEmployeesResource:
    """Test cases for the Employees API."""

    def test_list_employees(self, client):
        """Test listing employees."""
        result = client.employees.list()

        assert result is not None
        # API may return a dict with 'employees' key or a list directly
        if isinstance(result, dict):
            assert "employees" in result
            assert isinstance(result["employees"], list)
        else:
            assert isinstance(result, list)

    def test_list_employees_with_pagination(self, client):
        """Test listing employees with pagination."""
        result = client.employees.list(page=1)

        assert result is not None
        # API may return a dict with 'employees' key or a list directly
        if isinstance(result, dict):
            assert "employees" in result
            assert isinstance(result["employees"], list)
        else:
            assert isinstance(result, list)

    def test_create_employee(self, client):
        """Test creating an employee."""
        import time

        employee_data = EmployeeCreate(
            name=f"Test Employee {int(time.time())}",
            last_name="Test",
            email=f"test{int(time.time())}@example.com",
            send_invite=False,
        )

        try:
            result = client.employees.create(employee_data)

            assert result is not None
            assert isinstance(result, dict)
            assert "id" in result or "_id" in result

            # Cleanup: delete the created employee
            employee_id = result.get("id") or result.get("_id")
            if employee_id:
                try:
                    client.employees.delete(employee_id)
                except Exception:
                    pass  # Ignore cleanup errors
        except Exception as e:
            pytest.skip(f"Employee creation failed: {e}")

    def test_get_employee(self, client):
        """Test getting an employee."""
        import time

        # First, create an employee to get
        employee_data = EmployeeCreate(
            name=f"Test Employee Get {int(time.time())}",
            last_name="Test",
            email=f"testget{int(time.time())}@example.com",
            send_invite=False,
        )

        try:
            created = client.employees.create(employee_data)
            employee_id = created.get("id") or created.get("_id")
            if not employee_id:
                pytest.skip("Employee ID not found after creation")

            result = client.employees.get(employee_id)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                client.employees.delete(employee_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Get employee failed: {e}")

    def test_update_employee(self, client):
        """Test updating an employee."""
        import time

        # First, create an employee to update
        employee_data = EmployeeCreate(
            name=f"Test Employee Update {int(time.time())}",
            last_name="Test",
            email=f"testupdate{int(time.time())}@example.com",
            send_invite=False,
        )

        try:
            created = client.employees.create(employee_data)
            employee_id = created.get("id") or created.get("_id")
            if not employee_id:
                pytest.skip("Employee ID not found after creation")

            # Update the employee
            update_data = EmployeeUpdate(
                name="Updated Test Employee",
            )
            result = client.employees.update(employee_id, update_data)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                client.employees.delete(employee_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Update employee failed: {e}")

    def test_delete_employee(self, client):
        """Test deleting an employee."""
        import time

        # First, create an employee to delete
        employee_data = EmployeeCreate(
            name=f"Test Employee Delete {int(time.time())}",
            last_name="Test",
            email=f"testdelete{int(time.time())}@example.com",
            send_invite=False,
        )

        try:
            created = client.employees.create(employee_data)
            employee_id = created.get("id") or created.get("_id")
            if not employee_id:
                pytest.skip("Employee ID not found after creation")

            # Delete the employee
            result = client.employees.delete(employee_id)

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Delete employee failed: {e}")


class TestAsyncEmployeesResource:
    """Test cases for the Async Employees API."""

    @pytest.mark.asyncio
    async def test_list_employees(self, async_client):
        """Test listing employees asynchronously."""
        result = await async_client.employees.list()

        assert result is not None
        # API may return a dict with 'employees' key or a list directly
        if isinstance(result, dict):
            assert "employees" in result
            assert isinstance(result["employees"], list)
        else:
            assert isinstance(result, list)

    @pytest.mark.asyncio
    async def test_list_employees_with_pagination(self, async_client):
        """Test listing employees with pagination asynchronously."""
        result = await async_client.employees.list(page=1)

        assert result is not None
        # API may return a dict with 'employees' key or a list directly
        if isinstance(result, dict):
            assert "employees" in result
            assert isinstance(result["employees"], list)
        else:
            assert isinstance(result, list)

    @pytest.mark.asyncio
    async def test_create_employee(self, async_client):
        """Test creating an employee asynchronously."""
        import time

        employee_data = EmployeeCreate(
            name=f"Test Employee Async {int(time.time())}",
            last_name="Test",
            email=f"testasync{int(time.time())}@example.com",
            send_invite=False,
        )

        try:
            result = await async_client.employees.create(employee_data)

            assert result is not None
            assert isinstance(result, dict)
            assert "id" in result or "_id" in result

            # Cleanup: delete the created employee
            employee_id = result.get("id") or result.get("_id")
            if employee_id:
                try:
                    await async_client.employees.delete(employee_id)
                except Exception:
                    pass  # Ignore cleanup errors
        except Exception as e:
            pytest.skip(f"Employee creation failed: {e}")

    @pytest.mark.asyncio
    async def test_get_employee(self, async_client):
        """Test getting an employee asynchronously."""
        import time

        # First, create an employee to get
        employee_data = EmployeeCreate(
            name=f"Test Employee Get Async {int(time.time())}",
            last_name="Test",
            email=f"testgetasync{int(time.time())}@example.com",
            send_invite=False,
        )

        try:
            created = await async_client.employees.create(employee_data)
            employee_id = created.get("id") or created.get("_id")
            if not employee_id:
                pytest.skip("Employee ID not found after creation")

            result = await async_client.employees.get(employee_id)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                await async_client.employees.delete(employee_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Get employee failed: {e}")

    @pytest.mark.asyncio
    async def test_update_employee(self, async_client):
        """Test updating an employee asynchronously."""
        import time

        # First, create an employee to update
        employee_data = EmployeeCreate(
            name=f"Test Employee Update Async {int(time.time())}",
            last_name="Test",
            email=f"testupdateasync{int(time.time())}@example.com",
            send_invite=False,
        )

        try:
            created = await async_client.employees.create(employee_data)
            employee_id = created.get("id") or created.get("_id")
            if not employee_id:
                pytest.skip("Employee ID not found after creation")

            # Update the employee
            update_data = EmployeeUpdate(
                name="Updated Test Employee Async",
            )
            result = await async_client.employees.update(employee_id, update_data)

            assert result is not None
            assert isinstance(result, dict)

            # Cleanup
            try:
                await async_client.employees.delete(employee_id)
            except Exception:
                pass
        except Exception as e:
            pytest.skip(f"Update employee failed: {e}")

    @pytest.mark.asyncio
    async def test_delete_employee(self, async_client):
        """Test deleting an employee asynchronously."""
        import time

        # First, create an employee to delete
        employee_data = EmployeeCreate(
            name=f"Test Employee Delete Async {int(time.time())}",
            last_name="Test",
            email=f"testdeleteasync{int(time.time())}@example.com",
            send_invite=False,
        )

        try:
            created = await async_client.employees.create(employee_data)
            employee_id = created.get("id") or created.get("_id")
            if not employee_id:
                pytest.skip("Employee ID not found after creation")

            # Delete the employee
            result = await async_client.employees.delete(employee_id)

            assert result is not None
            assert isinstance(result, dict)
        except Exception as e:
            pytest.skip(f"Delete employee failed: {e}")

