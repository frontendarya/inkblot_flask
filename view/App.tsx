import React from "react";
import { Routes, Route } from "react-router-dom";
import "./App.css";
import MainPage from "./pages/MainPage/MainPage";
import TestPage from "./pages/TestPage/TestPage";
import { ResultPage } from "./pages/ResultPage/ResultPage";

function App() {
  return (
    <div>
      <Routes>
        <Route path="/" element={<MainPage />}></Route>
        <Route path="/test" element={<TestPage />}></Route>
        <Route path="/result" element={<ResultPage />}></Route>
      </Routes>
    </div>
  );
}

export default App;
