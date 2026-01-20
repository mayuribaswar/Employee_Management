import { useState } from "react";
import { addEmployee } from "../services/api";

function EmployeeForm({ refresh }) {
  const [form, setForm] = useState({
    name: "",
    email: "",
    salary: "",
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    await addEmployee(form);
    setForm({ name: "", email: "", salary: "" });
    refresh();
  };

  return (
    <div className="card">
      <h2>Add Employee</h2>
      <form onSubmit={handleSubmit}>
        <input
          name="name"
          placeholder="Name"
          value={form.name}
          onChange={handleChange}
          required
        />
        <input
          name="email"
          placeholder="Email"
          value={form.email}
          onChange={handleChange}
          required
        />
        <input
          name="salary"
          placeholder="Salary"
          value={form.salary}
          onChange={handleChange}
          required
        />
        <button type="submit">Add</button>
      </form>
    </div>
  );
}

export default EmployeeForm;
