const React5 = () => {
  const array = ["dog", "cat", "chicken", "cow", "sheep", "horse"];

  const createArray = () => {
    return array.map((item) => {
      return <li>{item}</li>;
    });
  };

  return (
    <div className="flex flex-col justify-center text-center items-center my-10">
      <p className="text-xl px-40 mb-4">
        Exercise 5: Mapping Through A List And Rendering To get comfortable with
        React, you must learn declarative programming. React is declarative. So
        you need to think in "declarative programming" whenever you work with
        React, and this exercise is perfect for that. This is the "opposite" of
        imperative programming which is the paradigm used in Vanilla JavaScript.
        In this exercise, instead of manually and "imperatively" coding the
        render of each item in a list, use the map function to "declare" how
        React should render the list.
      </p>
      <div>{createArray()}</div>
    </div>
  );
};

export default React5;
