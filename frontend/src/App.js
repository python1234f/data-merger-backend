import React, { useState, useEffect } from "react";
import Progress from 'react-progressbar';
import { v4 as uuidv4 } from "uuid";
import './App.css';

function App() {
  const [tasks, setTasks] = useState([]);
  // const backendHost = process.env.REACT_APP_BACKEND_HOSTNAME;
  // const backendPort = process.env.REACT_APP_BACKEND_PORT;

  const backendHost = "localhost";
  const backendPort = "8888";

  const wsUrl = `ws://${backendHost}:${backendPort}/tasks/`;
  const httpUrl = `http://${backendHost}:${backendPort}/api/task/`;

  useEffect(() => {
    const socket = new WebSocket(wsUrl);
    socket.onmessage = (event) => {
      const message = JSON.parse(event.data);
      if(message.status === "PROGRESS") {
        updateTaskProgress(message.id, message.payload.progress);
      }
    };
  }, []);

  const updateTaskProgress = (taskId, progress) => {
    setTasks(prevTasks =>
      prevTasks.map(task =>
        task.id === taskId ? { ...task, progress } : task
      )
    );
  };

  const startTask = async () => {
    const id = "task_" + uuidv4();
    const response = await fetch(httpUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ id }),
    });

    if (response.status === 201) {
      setTasks(prevTasks => [...prevTasks, { id, progress: 0 }]);
    }
  };

  return (
    <div className="App">
      <button className="start-button" onClick={startTask}>Start Task</button>
      {tasks.map(task => (
        <div key={task.id}>
          <h2>{task.id}</h2>
          <h3>{task.progress * 100} %</h3>
          <Progress completed={task.progress * 100} />
          {/*<ProgressBar progress={String(task.progress * 100)} />*/}
        </div>
      ))}
    </div>
  );
}

export default App;