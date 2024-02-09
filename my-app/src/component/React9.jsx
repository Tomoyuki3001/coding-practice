const React8 = () => {
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
        Exercise 9: Working with an API Last but definitely not the least, work
        with an API and build a simple frontend:
      </p>
      {createRender()}
    </div>
  );
};

export default React8;
