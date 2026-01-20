import { useState } from "react";
import { deleteEmployee, updateEmployee } from "../services/api";

function EmployeeList({ employees, refresh }) {
  const [editId, setEditId] = useState(null);
  const [editData, setEditData] = useState({});

  const startEdit = (emp) => {
    setEditId(emp.id);
    setEditData(emp);
  };

  const saveEdit = async () => {
    await updateEmployee(editId, editData);
    setEditId(null);
    refresh();
  };

  return (
    <div className="card">
      <h2>Employees</h2>

      {employees.map((emp) => (
        <div key={emp.id} className="row">
          {editId === emp.id ? (
            <>
              <input
                value={editData.name}
                onChange={(e) =>
                  setEditData({ ...editData, name: e.target.value })
                }
              />
              <input
                value={editData.email}
                onChange={(e) =>
                  setEditData({ ...editData, email: e.target.value })
                }
              />
              <input
                value={editData.salary}
                onChange={(e) =>
                  setEditData({ ...editData, salary: e.target.value })
                }
              />
              <button onClick={saveEdit}>Save</button>
            </>
          ) : (
            <>
              <span>{emp.name}</span>
              <span>{emp.email}</span>
              <span>₹{emp.salary}</span>
              <button onClick={() => startEdit(emp)}>Edit</button>
              <button onClick={() => deleteEmployee(emp.id).then(refresh)}>
                Delete
              </button>
            </>
          )}
        </div>
      ))}
    </div>
  );
}

export default EmployeeList;
