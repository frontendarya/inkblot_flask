import React from "react";
import { useNavigate } from "react-router-dom";
import "./MainPage.css";

const MainPage: React.FC = () => {
  const navigate = useNavigate();

  const handleStartClick = () => {
    navigate("/test");
  };

  return (
    <div className="main-page">
      <div className="image-filter"></div>
      <div className="container">
        <h1 className="title">RORSCHACH INKBLOT TEST</h1>
        <div className="info">
          Данное приложение не ставит диагнозы и не даёт точную диагностику,
          используйте его исключительно в развлекательных целях. Сейчас перед
          вами появятся 10 картинок, вам нужно будет внимательно их рассмотреть
          и ответить на вопросы. Можно дать один ответ, несколько или вообще
          отказаться от ответа.
        </div>
        <a onClick={handleStartClick} className="btn">
          Начать
        </a>
      </div>
    </div>
  );
};

export default MainPage;
