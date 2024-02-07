import React from "react";

const React1 = () => {
  return (
    <div className="flex flex-col justify-center text-center items-center">
      <p className="text-xl px-40 mb-4">
        Exercise 1: Hello World! Every programming language starter tutorial
        teaches you how to output "Hello, World!" using the language. <br />
        But this exercise is not just for tradition. This will asses if you
        actually know HTML, which is one of the many prerequisites before
        learning React. <br />
        Start by rendering a square with a background color. Inside the square,
        render "Hello, World!".
      </p>
      <a
        href="https://coderfiles.dev/blog/reactjs-coding-exercises/"
        target="_blank"
        rel="noreferrer"
      >
        <p className="mb-4 text-blue-400 text-xl">Exercise link</p>
      </a>
      <div className="bg-orange-400 w-20 h-20 flex justify-center text-center items-center p-20">
        <p>Hello World!</p>
      </div>
    </div>
  );
};

export default React1;
