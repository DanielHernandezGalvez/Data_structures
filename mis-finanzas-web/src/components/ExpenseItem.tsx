import React from "react";
import { Expense } from "../interfaces/Expense";

interface ExpenseItemProps {
  expense: Expense;
  onEdit: (id: number) => void;
  onDelete: (id: number) => void;
}

const ExpenseItem: React.FC<ExpenseItemProps> = ({
  expense,
  onEdit,
  onDelete,
}) => {
  return (
    <div>
      <p>{expense.description}</p>
      <p>${expense.amount}</p>
      <p>{expense.date}</p>
      <button onClick={() => onEdit(expense.id)}>Editar</button>
      <button onClick={() => onDelete(expense.id)}>Eliminar</button>
    </div>
  );
};

export default ExpenseItem;
