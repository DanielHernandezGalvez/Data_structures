import React from "react";
import { Header as Head, Icon } from "semantic-ui-react";
const Header = () => {
  return (
    <div className="header marging">
      <Head as="h1" icon textAlign="center" color="yellow">
        <Icon inverted color="yellow" name="list alternate outline" circular />
        <Head.Content className="marging">Listado de tareas</Head.Content>
      </Head>
    </div>
  );
};

export default Header;
