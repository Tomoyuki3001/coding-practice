import { useState } from "react";

const React7 = () => {
  const [first, setFirst] = useState("");
  const [last, setLast] = useState("");

  const getNames = () => {
    alert(`Hello ${first} ${last}`);
    setFirst("");
    setLast("");
  };
  return (
    <div className="flex flex-col justify-center text-center items-center my-10">
      <p className="text-xl px-40 mb-4">
        Exercise 6: Mapping Through A List And Rendering (With A Custom
        Component) In exercise 3, we mentioned that part of what makes React so
        great is that it allows us to create our custom, re-usable components.
        You only created a custom button there. This time, you'll create a
        custom component that displays each item from exercise 5:
      </p>
      <div className="flex flex-col">
        <input
          className="border"
          type="text"
          placeholder="First name"
          onChange={(e) => setFirst(e.target.value)}
        />
        <input
          className="border"
          type="text"
          placeholder="Last name"
          onChange={(e) => setLast(e.target.value)}
        />
        <button onClick={getNames} className="mt-4 py-2 px-4 bg-blue-400">
          GREET ME
        </button>
      </div>
    </div>
  );
};

export default React7;
