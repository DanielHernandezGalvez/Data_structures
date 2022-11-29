import React from "react";
import { Select, Input, Button, Grid, Header, Icon } from "semantic-ui-react";
import { useState } from "react";
import { v4 as uuidv4 } from "uuid";

const options = [
  { key: "Algoritmos", text: "Algoritmos", value: "Algoritmos" },
  { key: "JavaScript", text: "JavaScript", value: "JavaScript" },
  { key: "DOM", text: "DOM", value: "DOM" },
  { key: "React", text: "React", value: "React" },
  { key: "Redux", text: "Redux", value: "Redux" },
  { key: "Node", text: "Node", value: "Node" },
  { key: "Express", text: "Express", value: "Express" },
  { key: "SQL", text: "SQL", value: "SQL" },
];
const InputTask = (props) => {
  const [task, setTask] = useState({
    idTask: "",
    taskName: "",
    categoryTask: "",
  });
  const [error, setError] = useState(false);

  const { createTask } = props;

  const onChangeTask = (e) => {
    setTask({
      ...task,
      [e.target.name]: e.target.value,
    });
  };

  const onchangeCategoryTask = (e, data) => {
    setTask({
      ...task,
      [data.name]: data.value,
    });
  };

  const onSubmitTask = (e) => {
    //no recargar página
    e.preventDefault();

    //validación de inputs
    if (task.taskName.trim() === "" || task.categoryTask.trim() === "") {
      setError(true);
      return;
    }

    //eliminar mensaje previo
    setError(false);

    //asignar id
    task.idTask = uuidv4();

    //crear task
    createTask(task);

    //limpiar inputs
    setTask({
      idTask: "",
      taskName: "",
      categoryTask: "",
    });
  };

  return (
    <>
      <Grid centered column={2}>
        <Input type="text" action>
          <Input
            size="small"
            icon="add"
            placeholder="Escribe tu tarea..."
            iconPosition="left"
            name="taskName"
            value={task.taskName}
            onChange={onChangeTask}
          />
          <Select
            compact
            options={options}
            className="select-form-task "
            name="categoryTask"
            placeholder="Categoría"
            value={task.categoryTask}
            onChange={onchangeCategoryTask}
          />
          <Button type="submit" color="yellow" onClick={onSubmitTask}>
            Añadir tarea
          </Button>
        </Input>
      </Grid>
      {error && (
        <Grid centered className="marging">
          <Header as="h4" color="red" className="alert-error-form">
            <Icon name="close" />
            <Header.Content>La tarea es obligatoria</Header.Content>
            <Icon name="close" />
          </Header>
        </Grid>
      )}
    </>
  );
};

export default InputTask;
