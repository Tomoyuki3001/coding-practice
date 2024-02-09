const React9 = () => {
  const arrayObject = [
    {
      id: 1,
      setup: "What's the best thing about a Boolean?",
      punchline: "Even if you're wrong, you're only off by a bit",
    },
    {
      id: 2,
      setup: "Why do programmers wear glasses?",
      punchline: "Because they need to C#",
    },
  ];

  const createRender = () => {
    return arrayObject.map((obj) => {
      return (
        <div className="mt-4 flex flex-col items-center">
          <div>Setup: {obj.setup}</div>
          <div>Punch line: {obj.punchline}</div>
        </div>
      );
    });
  };
  return (
    <div className="flex flex-col justify-center text-center items-center my-10">
      <p className="text-xl px-40 mb-4">
        Exercise 8: Rendering JSON Most of the time, the structure of the data
        we're working with in real-world applications aren't simple lists like
        ['dog', 'cat', 'chicken', 'cow', 'sheep', 'horse']. A lot of data is
        stored in JSON format. This is especially true when you're fetching data
        from a database. JSON stands for JavaScript Object Notation, a type of
        format for data interchange. This type of data is just an object instead
        of a simpler datatype such as a string. For example, an array of JSON
        objects looks like this:item from exercise 5:
      </p>
      {createRender()}
    </div>
  );
};

export default React9;
