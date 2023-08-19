import { Expense } from "./Expense";

export interface ExpenseListProps {
  expenses: Expense[];
  onEdit: (id: number) => void;
  onDelete: (id: number) => void;
}
