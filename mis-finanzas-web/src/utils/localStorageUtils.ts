import { Expense } from "../interfaces/Expense";
const STORAGE_KEY = "expenses";

export const getExpensesFromLocalStorage = (): Expense[] => {
  const expensesJSON = localStorage.getItem(STORAGE_KEY);
  return expensesJSON ? JSON.parse(expensesJSON) : [];
};

export const saveExpensesToLocalStorage = (expenses: Expense[]): void => {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(expenses));
};
