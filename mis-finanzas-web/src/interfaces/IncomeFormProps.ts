export interface IncomeFormProps {
  incomes: string;
  type: string;
  onSubmit: (description: string, amount: number, date: string) => void;
}
