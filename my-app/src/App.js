import React1 from "./component/React1";
import React2 from "./component/React2";
import React3 from "./component/React3";
import React4 from "./component/React4";

function App() {
  return (
    <div className="flex flex-col justify-center text-center items-center px-40 pt-20">
      <h1 className="text-2xl font-bold mb-4">React Coding Practice</h1>
      <React1 />
      <React2 />
      <React3 />
      <React4 />
    </div>
  );
}

export default App;
