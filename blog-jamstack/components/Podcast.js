import React from "react";
import Image from "next/image";
import Head from "next/head";
import Pod from "./Recurso 1.png";

export const Podcast = ({ episode }) => {
  return (
    <div>
      <Head>
        <title>Segundo</title>
      </Head>
      Este es el Podcast
      <br />
      <Image src={Pod} width={200} height={200} />
    </div>
  );
};
