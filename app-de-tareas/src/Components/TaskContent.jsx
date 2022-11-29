import React from "react";
import { Header, Icon, Grid } from "semantic-ui-react";
import Task from "./Task";


const TaskContent = (props) => {
  const { tasks, deleteTask } = props;

  if (tasks.length === 0) {
    return null;
  }



  return (
    <Grid className="tasks-content ">
      <Header
        as="h2"
        color="yellow"
        icon
        className="marging"
        textAlign="center"
      >
        <Icon name="settings" className="marging" />
        Administra tus tareas
      </Header>
      <Grid.Row>
        {tasks.map((task, index) => (
          <Task task={task} key={index} deleteTask={deleteTask}/>
        ))}
      </Grid.Row>
    </Grid>
  );
};

export default TaskContent;
