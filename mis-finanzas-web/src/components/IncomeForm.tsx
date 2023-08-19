import React, { useState } from "react";

interface IncomeFormProps {
  type: string;
  onSubmit: (description: string, amount: number, date: string) => void;
}

const IncomeForm: React.FC<IncomeFormProps> = ({ type, onSubmit }) => {
  const [description, setDescription] = useState("");
  const [amount, setAmount] = useState(0);
  const [date, setDate] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit(description, amount, date);
    setDescription("");
    setAmount(0);
    setDate("");
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Ingresar {type}</h2>
      <input
        type="text"
        placeholder="Descripción"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />
      <input
        type="number"
        placeholder="Cantidad"
        value={amount}
        onChange={(e) => setAmount(parseFloat(e.target.value))}
      />
      <input
        type="date"
        value={date}
        onChange={(e) => setDate(e.target.value)}
      />
      <button type="submit">Agregar {type}</button>
    </form>
  );
};

export default IncomeForm;
