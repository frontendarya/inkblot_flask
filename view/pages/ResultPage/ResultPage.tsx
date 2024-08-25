import react from "react";
import "./ResultPage.css";
import { useNavigate } from "react-router-dom";
export function ResultPage() {
  const score1 = "Текст для результата 1";
  const score2 = "Текст для результата 2";
  const score3 = "Текст для результата 3";
  const score4 = "Текст для результата 4";
  const navigate = useNavigate();

  const handleRestartTest = () => {
    navigate("/test");
  };

  return (
    <div>
      <section className="result">
        <div className="header-result">
          <h1 className="title">RESULTS</h1>
          <p className="txt_start">
            Не воспринимайте серьёзно результаты теста, полученные без участия
            специалиста
          </p>
        </div>
        <div className="body-result">
          <div className="res-block">
            <div className="category">
              <h3>Общая оценка личности</h3>
              <p className="txt-cat">
                Высокие показатели по некоторым детерминантам имеют свой
                психологический смысл
              </p>
            </div>
            <div className="score">
              <p className="txt-score">{score1}</p>
            </div>
          </div>
          <div className="res-block">
            <div className="category">
              <h3>Тип переживания</h3>
              <p className="txt-cat">
                Определяет характер взаимодействия с внешним миром, уровень
                эмпатии, интенсивность рефлексии
              </p>
            </div>
            <div className="score">
              <p className="txt-score">{score2}</p>
            </div>
          </div>
          <div className="res-block">
            <div className="category">
              <h3>Механизамы защиты</h3>
              <p className="txt-cat">
                Отпределяет наличие конфликта (тревожность, стресс, апатия), а
                также механизм психологической защиты
              </p>
            </div>
            <div className="score">
              <p className="txt-score">{score3}</p>
            </div>
          </div>
          <div className="res-block">
            <div className="category">
              <h3>Интеллектуальные возможности</h3>
              <p className="txt-cat">
                Тест Роршаха не даёт оценку интеллектуальным способностям,
                однако могут дать оценку гибкости ума
              </p>
            </div>
            <div className="score">
              <p className="txt-score">{score4}</p>
            </div>
          </div>
        </div>
        <div className="restart-button">
          <button onClick={handleRestartTest}>Пройти тест заново</button>
        </div>
      </section>
    </div>
  );
}
