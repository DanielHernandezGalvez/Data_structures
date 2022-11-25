import { useState } from 'react';

export default function Welcome(props) {
    const [ counter, setCounter ] = useState(0)
  const { message } = props;

  return (
    <div>
      <p>Hola desde weo¿lcome</p>
      <h2>contador con hooks</h2>
      <h4>El numero es {counter}</h4>
      <button type='submit' onClick={() => setCounter(counter + 1)}>sumar contador</button>
    </div>
  );
}
