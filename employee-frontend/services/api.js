const BASE_URL = "http://localhost:5000";

// GET all employees
export const getEmployees = async () => {
  const res = await fetch(`${BASE_URL}/employees`);
  return res.json();
};

// ADD employee
export const addEmployee = async (employee) => {
  const res = await fetch(`${BASE_URL}/employees`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(employee),
  });
  return res.json();
};

// UPDATE employee (PATCH)
export const updateEmployee = async (id, data) => {
  const res = await fetch(`${BASE_URL}/employees/${id}`, {
    method: "PATCH",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return res.json();
};

// DELETE employee
export const deleteEmployee = async (id) => {
  const res = await fetch(`${BASE_URL}/employees/${id}`, {
    method: "DELETE",
  });
  return res.json();
};
