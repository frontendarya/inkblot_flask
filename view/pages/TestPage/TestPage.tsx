import React, { useState } from "react";
import "./TestPage.css";
import image1 from "../data/cards/1.jpg";
import image2 from "../data/cards/2.jpg";
import image3 from "../data/cards/3.jpg";
import image4 from "../data/cards/4.jpg";
import image5 from "../data/cards/5.jpg";
import image6 from "../data/cards/6.jpg";
import image7 from "../data/cards/7.jpg";
import image8 from "../data/cards/8.jpg";
import image9 from "../data/cards/9.jpg";
import image10 from "../data/cards/10.jpg";
import { useNavigate } from "react-router-dom";
interface Response {
  cardNumber: number;
  imageDescription: string;
  hasClearForm: boolean | null;
  isInMotion: boolean | null;
  seenIn: string;
  influence: string;
}

const images = [
  image1,
  image2,
  image3,
  image4,
  image5,
  image6,
  image7,
  image8,
  image9,
  image10,
];

const TestPage: React.FC = () => {
  const [cardNumber, setCardNumber] = useState(1);
  const [responses, setResponses] = useState<Response[]>([]);
  const [formData, setFormData] = useState({
    imageDescription: "",
    hasClearForm: null as boolean | null,
    isInMotion: null as boolean | null,
    seenIn: "",
    influence: "",
  });
  const navigate = useNavigate();
  const changeImage = (skipResponse = false) => {
    const newResponse: Response = {
      cardNumber,
      ...formData,
    };

    setResponses((prevResponses) => {
      const updatedResponses = skipResponse
        ? [
            ...prevResponses,
            {
              cardNumber,
              imageDescription: "",
              hasClearForm: null,
              isInMotion: null,
              seenIn: "",
              influence: "",
            },
          ]
        : [...prevResponses, newResponse];
      console.log("Responses:", updatedResponses);
      return updatedResponses;
    });

    // Сбрасываем поля
    setCardNumber(cardNumber < 10 ? cardNumber + 1 : 1);
    setFormData({
      imageDescription: "",
      hasClearForm: null,
      isInMotion: null,
      seenIn: "",
      influence: "",
    });

    if (cardNumber === 10) {
      navigate("/result");
    }
  };

  const addAdditionalResponse = () => {
    const newResponse: Response = {
      cardNumber,
      ...formData,
    };

    setResponses((prevResponses) => {
      const updatedResponses = [...prevResponses, newResponse];
      console.log("Responses:", updatedResponses);
      return updatedResponses;
    });

    setFormData({
      imageDescription: "",
      hasClearForm: null,
      isInMotion: null,
      seenIn: "",
      influence: "",
    });
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value, type, checked } = e.target;
    const val = type === "radio" ? checked : value;
    setFormData({
      ...formData,
      [name]: val,
    });
  };

  return (
    <section id="test" className="test">
      <div className="card-block">
        <div className="left_side">
          <p className="card" id="number">
            {cardNumber}/10
          </p>
          <img
            src={images[cardNumber - 1]}
            id="testImage"
            className="img-test"
            alt="тестовое изображение"
          />
          <div className="btn-group">
            <button className="btn_test" onClick={() => changeImage(true)}>
              Не отвечать на карточку
            </button>
            <button className="btn_test" onClick={addAdditionalResponse}>
              Дополнительный ответ
            </button>
            <button className="btn_test" onClick={() => changeImage(false)}>
              Следующая карточка
            </button>
          </div>
        </div>
        <div className="right_side">
          <div>
            <p className="txt">1. Что Вы видите на карточке? Опишите</p>
            <div className="answer">
              <input
                type="text"
                id="fieldAnswer"
                name="imageDescription"
                className="textArea"
                placeholder="Опишите картинку"
                value={formData.imageDescription}
                onChange={handleChange}
              />
            </div>
          </div>

          <div>
            <p className="txt">2. Увиденное имеет чёткую форму?</p>
            <div className="answer">
              <input
                type="radio"
                id="radioyes2"
                name="hasClearForm"
                className="my-radio"
                checked={formData.hasClearForm === true}
                onChange={() =>
                  setFormData({ ...formData, hasClearForm: true })
                }
              />
              <label htmlFor="radioyes2" className="txt">
                Да
              </label>
            </div>
            <div className="answer">
              <input
                type="radio"
                id="radiono2"
                name="hasClearForm"
                className="my-radio"
                checked={formData.hasClearForm === false}
                onChange={() =>
                  setFormData({ ...formData, hasClearForm: false })
                }
              />
              <label htmlFor="radiono2" className="txt">
                Нет
              </label>
            </div>
          </div>

          <div>
            <p className="txt">
              3. Увиденное находится в движении? Например, объект плывёт, бежит
              или летит.
            </p>
            <div className="answer">
              <input
                type="radio"
                id="radioyes3"
                name="isInMotion"
                className="my-radio"
                checked={formData.isInMotion === true}
                onChange={() => setFormData({ ...formData, isInMotion: true })}
              />
              <label htmlFor="radioyes3" className="txt">
                Да
              </label>
            </div>
            <div className="answer">
              <input
                type="radio"
                id="radiono3"
                name="isInMotion"
                className="my-radio"
                checked={formData.isInMotion === false}
                onChange={() => setFormData({ ...formData, isInMotion: false })}
              />
              <label htmlFor="radiono3" className="txt">
                Нет
              </label>
            </div>
          </div>

          <div>
            <p className="txt">4. В какой части карточки Вы увидели образ?</p>
            <div className="answer">
              <input
                type="radio"
                id="radio1"
                name="seenIn"
                className="my-radio"
                checked={
                  formData.seenIn === "Всё изображение или большая его часть"
                }
                onChange={() =>
                  setFormData({
                    ...formData,
                    seenIn: "Всё изображение или большая его часть",
                  })
                }
              />
              <label htmlFor="radio1" className="txt">
                Всё изображение или большая его часть
              </label>
            </div>
            <div className="answer">
              <input
                type="radio"
                id="radio2"
                name="seenIn"
                className="my-radio"
                checked={formData.seenIn === "Часть большого пятна"}
                onChange={() =>
                  setFormData({ ...formData, seenIn: "Часть большого пятна" })
                }
              />
              <label htmlFor="radio2" className="txt">
                Часть большого пятна
              </label>
            </div>
            <div className="answer">
              <input
                type="radio"
                id="radio3"
                name="seenIn"
                className="my-radio"
                checked={
                  formData.seenIn === "Отдельные пятна или мелкие детали"
                }
                onChange={() =>
                  setFormData({
                    ...formData,
                    seenIn: "Отдельные пятна или мелкие детали",
                  })
                }
              />
              <label htmlFor="radio3" className="txt">
                Отдельные пятна или мелкие детали
              </label>
            </div>
            <div className="answer">
              <input
                type="radio"
                id="radio4"
                name="seenIn"
                className="my-radio"
                checked={formData.seenIn === "Белый фон"}
                onChange={() =>
                  setFormData({ ...formData, seenIn: "Белый фон" })
                }
              />
              <label htmlFor="radio4" className="txt">
                Белый фон
              </label>
            </div>
          </div>

          <div>
            <p className="txt">5. На ваш ответ повлияли цвет или форма?</p>
            <div className="answer">
              <input
                type="radio"
                id="radio5"
                name="influence"
                className="my-radio"
                checked={formData.influence === "Важнее форма, цвет вторичен"}
                onChange={() =>
                  setFormData({
                    ...formData,
                    influence: "Важнее форма, цвет вторичен",
                  })
                }
              />
              <label htmlFor="radio5" className="txt">
                Важнее форма, цвет вторичен
              </label>
            </div>
            <div className="answer">
              <input
                type="radio"
                id="radio6"
                name="influence"
                className="my-radio"
                checked={formData.influence === "Важнее цвет, форма вторична"}
                onChange={() =>
                  setFormData({
                    ...formData,
                    influence: "Важнее цвет, форма вторична",
                  })
                }
              />
              <label htmlFor="radio6" className="txt">
                Важнее цвет, форма вторична
              </label>
            </div>
            <div className="answer">
              <input
                type="radio"
                id="radio7"
                name="influence"
                className="my-radio"
                checked={formData.influence === "Важен только цвет"}
                onChange={() =>
                  setFormData({ ...formData, influence: "Важен только цвет" })
                }
              />
              <label htmlFor="radio7" className="txt">
                Важен только цвет
              </label>
            </div>
            <div className="answer">
              <input
                type="radio"
                id="radio8"
                name="influence"
                className="my-radio"
                checked={formData.influence === "Важна только форма"}
                onChange={() =>
                  setFormData({ ...formData, influence: "Важна только форма" })
                }
              />
              <label htmlFor="radio8" className="txt">
                Важна только форма
              </label>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default TestPage;
