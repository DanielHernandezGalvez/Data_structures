import React, { useState, useEffect } from "react";

interface Transaction {
  id: number;
  description: string;
  amount: number;
  type: "income" | "expense";
}

const App: React.FC = () => {
  const [transactions, setTransactions] = useState<Transaction[]>([]);
  const [description, setDescription] = useState("");
  const [amount, setAmount] = useState(0);
  const [type, setType] = useState<"income" | "expense">("income");

  useEffect(() => {
    const storedTransactions = localStorage.getItem("transactions");
    if (storedTransactions) {
      setTransactions(JSON.parse(storedTransactions));
    }
  }, []);

  useEffect(() => {
    localStorage.setItem("transactions", JSON.stringify(transactions));
  }, [transactions]);

  const handleAddTransaction = () => {
    const newTransaction: Transaction = {
      id: Date.now(),
      description,
      amount,
      type,
    };

    setTransactions([...transactions, newTransaction]);
    setDescription("");
    setAmount(0);
    setType("income");
  };

  const handleDeleteTransaction = (id: number) => {
    const updatedTransactions = transactions.filter(
      (transaction) => transaction.id !== id
    );
    setTransactions(updatedTransactions);
  };

  const totalIncome = transactions
    .filter((transaction) => transaction.type === "income")
    .reduce((total, transaction) => total + transaction.amount, 0);

  const totalExpense = transactions
    .filter((transaction) => transaction.type === "expense")
    .reduce((total, transaction) => total + transaction.amount, 0);

  useEffect(() => {
    localStorage.setItem("totalIncome", totalIncome.toString());
    localStorage.setItem("totalExpense", totalExpense.toString());
  }, [totalIncome, totalExpense]);

  const savedTotalIncome = localStorage.getItem("totalIncome");
  const savedTotalExpense = localStorage.getItem("totalExpense");

  return (
    <div>
      <h1>Expense and Income Calculator</h1>
      <div>
        <input
          type="text"
          placeholder="Description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />
        <input
          type="number"
          placeholder="Amount"
          value={amount}
          onChange={(e) => setAmount(parseFloat(e.target.value))}
        />
        <select
          value={type}
          onChange={(e) => setType(e.target.value as "income" | "expense")}
        >
          <option value="income">Income</option>
          <option value="expense">Expense</option>
        </select>
        <button onClick={handleAddTransaction}>Add</button>
      </div>
      <div>
        <h2>Transaction List</h2>
        <ul>
          {transactions.map((transaction) => (
            <li key={transaction.id}>
              {transaction.description} - {transaction.amount} -{" "}
              {transaction.type}
              <button onClick={() => handleDeleteTransaction(transaction.id)}>
                Delete
              </button>
            </li>
          ))}
        </ul>
      </div>
      <div>
        <h2>Balance</h2>
        <p>Total Income: {savedTotalIncome || 0}</p>
        <p>Total Expense: {savedTotalExpense || 0}</p>
        <p>Balance: {Number(savedTotalIncome) - Number(savedTotalExpense)}</p>
      </div>
    </div>
  );
};

export default App;
