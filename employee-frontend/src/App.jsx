import { useEffect, useState } from "react";
import EmployeeForm from "./components/EmployeeForm";
import EmployeeList from "./components/EmployeeList";
import { getEmployees } from "./services/api";
import "./index.css";

function App() {
  const [employees, setEmployees] = useState([]);

  const loadEmployees = async () => {
    const data = await getEmployees();
    setEmployees(data);
  };

  useEffect(() => {
    loadEmployees();
  }, []);

  return (
    <div className="container">
      <h1>Employee Management System</h1>
      <EmployeeForm refresh={loadEmployees} />
      <EmployeeList employees={employees} refresh={loadEmployees} />
    </div>
  );
}

export default App;
