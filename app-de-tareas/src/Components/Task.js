import React from "react";
import { Grid, Header, Label, Icon, Button, Segment } from "semantic-ui-react";

const Task = (props) => {
  const { task, deleteTask } = props;
  const { idTask, taskName, categoryTask } = task;

  return (
    <Grid.Column width={8} className="task-container">
      <Segment className="marging">
        {categoryTask && (
          <Label color="teal" ribbon="right">
            {categoryTask}
          </Label>
        )}
        <Header as="h3" className="header-task">
          {taskName}
        </Header>
        <Header as="h5">{idTask}</Header>
        <Grid center columns={2}>
          <Grid.Column>
            <Button color="red" onClick={() => deleteTask(idTask)}>
              <Icon name="remove circle" />
              Eliminar
            </Button>
          </Grid.Column>
        </Grid>
      </Segment>
    </Grid.Column>
  );
};

export default Task;
