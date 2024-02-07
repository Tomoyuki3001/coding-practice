import React, { useState } from "react";

const React4 = () => {
  const [count, setCount] = useState(0);

  const counter = () => {
    setCount(count + 1);
    return count;
  };
  return (
    <div className="flex flex-col justify-center text-center items-center my-10">
      <p className="text-xl px-40 mb-4">
        Exercise 4: State and Props So you're comfortable working with props,
        congratulations! <br />
        Using props allows us to pass values or functions down to a child
        component. State is another integral concept we must learn in React.{" "}
        <br />
        It allows us to store values, and React automatically updates our UI
        when the values change. That's one of the many beautiful things with
        React. <br />
        We don't need to manually handle these things - React does the UI
        re-rendering for us when a value changes. But we must know how to use
        the state for this purpose. <br />
        This exercise is simple, and is a very common React tutorial out there.
        Use the useState React hook to track how many times a button is clicked,
        and display the number. The number must increment each time the button
        is clicked:
      </p>
      <div>
        <p>The button has been clicked: {count} times</p>
        <button className="px-8 py-4 bg-blue-200 mt-4" onClick={counter}>
          Click Me
        </button>
      </div>
    </div>
  );
};

export default React4;
