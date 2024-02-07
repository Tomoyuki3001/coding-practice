import React from "react";

const React2 = () => {
  const makeAlert = () => {
    alert("Clicked!");
  };
  return (
    <div className="flex flex-col justify-center text-center items-center mt-10">
      <p className="text-xl px-40 mb-4">
        Exercise 2: Capturing User Clicks What makes a web app different from a
        static website? <br />A web app is interactive. Of course, there's more
        to web apps than capturing clicks, but it's important to start from the
        basics.
        <br />
        This exercise gets you started with event handling, which is a basic
        concept not only in React but also in JavaScript (which is again another
        pre-requisite before learning React). <br />
        Using the native HTML button tag, capture the click event and alert the
        message, "Clicked!". Take note that capturing events such as clicks is
        done differently in React than it is in JavaScript.
      </p>
      <button className="px-8 py-4 bg-blue-200" onClick={makeAlert}>
        Click
      </button>
    </div>
  );
};

export default React2;
