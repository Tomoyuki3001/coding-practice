const EXercise1 = () => {
  //   const countLetters = (string) => {
  //     let exists = {};
  //     for (let i = 0; i < string.length; i++) {
  //       if (exists[string[i]]) {
  //         exists[string[i]] += 1;
  //       } else {
  //         exists[string[i]] = 1;
  //       }
  //     }

  //     for (let item in exists) {
  //         console.log("Item: " + item + "is" + exists[item]);
  //     }
  //   };

  //   countLetters("Canada");

  //   const checkPalindrome = () => {
  //     const palindrome = "abcdekedca";
  //     let array = palindrome.split("");
  //     let arrayLength = array.length - 1;
  //     const firstPart = array.slice(0, arrayLength / 2);
  //     const lastPart = array.slice(arrayLength / 2 + 1, array.length).reverse();

  //     if (firstPart.toString() === lastPart.toString()) {
  //       console.log("The value is palindrome");
  //     } else {
  //       console.log("The value is not palindrome");
  //     }
  //   };

  //   checkPalindrome();

  const checkMissingNumber = () => {
    const value = [1, 2, 3, 5, 7, 14];
    let emptyArray = [];
    for (let i = 1; i < Math.max(...value) + 1; i++) {
      emptyArray.push(i);
    }
  };

  checkMissingNumber();

  return (
    <div>
      <div>Exercise 1</div>
      <p>
        1. Write a code to display which character is coming how many times in a
        given string ?
      </p>
      <ul></ul>
    </div>
  );
};

export default EXercise1;
