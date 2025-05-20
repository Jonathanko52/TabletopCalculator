import { useState } from "react";
import "./App.css";
import axios from "axios";

function App() {
  const [count, setCount] = useState(0);

  const refreshList = () => {
    axios //Axios to send and receive HTTP requests
      .get("http://localhost:8000/api/tasks/")
      .then((res) => console.log({ taskList: res.data }))
      .catch((err) => console.log(err));
  };

  return (
    <div class="container-fluid py-5 h-100">
      <div class="row  h-25 mb-4 justify-content-center">
        <div class="col-9 h-50 border border-primary">
          <div class="box">Column 1</div>
        </div>
      </div>
      <div class="row justify-content-center h-75 g-3">
        <div class="col-2 m-4 border border-primary">
          <div class="box">Column 1</div>
        </div>
        <div class="col-2 m-4 border border-primary">
          <div class="box">Column 2</div>
        </div>
        <div class="col-2 m-4 border border-primary">
          <div class="box">Column 3</div>
        </div>
        <div class="col-2 m-4 border border-primary">
          <div class="box">Column 4</div>
        </div>
      </div>
      <button onClick={() => refreshList()}>Fetch Tasks</button>
    </div>
  );
}

export default App;
