import React from "react";

const React3 = () => {
  const buttonArray = ["Button1", "Button2", "Button3"];

  const buttons = () => {
    const buttonElements = buttonArray.map((button, index) => (
      <button
        key={index}
        className="px-8 py-4 bg-blue-200 ml-3"
        onClick={() => {
          alert(`This is the ${button}`);
        }}
      >
        {button}
      </button>
    ));
    return buttonElements;
  };

  return (
    <div className="flex flex-col justify-center text-center items-center mt-10">
      <p className="text-xl px-40 mb-4">
        Exercise 3: Custom Component In the previous exercise, we used the HTML
        button tag. <br />
        But much of the power that React provides to us developers is being able
        to create our own components and reuse them. <br />
        You'll be creating more complicated custom components than a simple
        button in the near future, but we all gotta start somewhere. <br />
        In this exercise, build your own Button component and render it three
        times. On user click, it should alert which button was clicked:
      </p>
      <div className="flex">{buttons()}</div>
    </div>
  );
};

export default React3;
