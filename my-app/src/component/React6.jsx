const React6 = () => {
  const animals = [
    { number: 1, name: "dog" },
    { number: 2, name: "cat" },
    { number: 3, name: "chicken" },
    { number: 4, name: "cow" },
    { number: 5, name: "sheep" },
    { number: 6, name: "horse" },
  ];
  return (
    <div className="flex flex-col justify-center text-center items-center my-10">
      <p className="text-xl px-40 mb-4">
        Exercise 6: Mapping Through A List And Rendering (With A Custom
        Component) In exercise 3, we mentioned that part of what makes React so
        great is that it allows us to create our custom, re-usable components.
        You only created a custom button there. This time, you'll create a
        custom component that displays each item from exercise 5:
      </p>
      <div>
        {animals.map((animal) => (
          <div>
            {animal.number} {animal.name}
          </div>
        ))}
      </div>
    </div>
  );
};

export default React6;
