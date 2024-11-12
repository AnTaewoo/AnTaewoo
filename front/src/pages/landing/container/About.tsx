import yoloImg from "@/assets/yolo-icon.svg";
import opencvImg from "@/assets/opencv-icon.png";
import reactImg from "@/assets/react-icon.png";
import bgImg from "@/assets/background-2.png";

import { useState } from "react";
interface ListType {
  img: string;
  title: string;
  description: string;
}

const list: ListType[] = [
  {
    img: yoloImg,
    title: "Yolo",
    description:
      "Yolo는 실시간 객체 인식을 위한 딥러닝 모델로, 비디오 피드에서 사용자의 위치와 주의 분산 여부를 빠르게 감지합니다. 이 모델을 통해 사용자의 시선과 동작을 인식해 학습 상태인지 판단할 수 있습니다.",
  },
  {
    img: opencvImg,
    title: "OpenCV",
    description:
      "OpenCV는 이미지와 비디오 처리에 유용한 라이브러리로, YOLO와 연동해 웹캠 피드를 처리하고 사용자의 위치와 얼굴을 추적할 수 있습니다. 비디오 프레임을 실시간으로 처리하며, 모델에 필요한 입력을 제공합니다.",
  },
  {
    img: reactImg,
    title: "React",
    description:
      "React는 사용자 UI를 구축하기 위한 라이브러리로, 실시간 학습 상태와 타이머 상태를 표시하는 데 사용됩니다. 사용자에게 현재 학습 여부, 타이머 상태를 직관적으로 전달하는 UI 컴포넌트를 제공합니다.",
  },
];

export default function About() {
  const [listActive, setListActive] = useState<number[]>([0, 0, 0]);
  const clickList = (index: number) => {
    const newListActive = listActive.map((active, i) =>
      i == index ? (active != 1 ? 1 : 0) : listActive[index] != 1 ? 2 : 0
    );

    setListActive(newListActive);
  };
  return (
    <div className=" w-full pt-36 pb-72">
      <div className=" relative w-full">
        <div className=" absolute top-0 -translate-y-96 left-0 w-full ">
          <img
            src={bgImg}
            alt="background-2"
            className=" w-full object-cover"
          />
        </div>
      </div>
      <div className=" w-full max-w-7xl mx-auto ">
        <div className=" w-full mb-10">
          <p className=" text-slate-50 text-5xl font-extrabold text-center leading-[80px] font-sans">
            Leveraging YOLO, OpenCV, and React for
            <br />
            Real-Time Distraction Detection and Timer Control
          </p>
        </div>
        <div className=" w-full flex gap-2 h-[600px] list-none">
          {list.map((value, index) => (
            <li
              key={index}
              className=" bg-slate-50 rounded-xl p-14 flex flex-col items-center transition-all duration-500 shrink-0"
              style={{
                width:
                  listActive[index] == 0
                    ? `${100 / listActive.length}%`
                    : listActive[index] == 1
                    ? "50%"
                    : `${50 / (listActive.length - 1)}%`,
                scale: listActive[index] == 1 ? "1.1" : "1",
                filter: listActive[index] != 2 ? "none" : "grayscale(100%)",
                opacity:
                  listActive[index] == 1
                    ? "1"
                    : listActive[index] == 2
                    ? "0.5"
                    : "0.95",
              }}
              onClick={() => clickList(index)}
            >
              <div className="w-60 h-60 mb-10 shrink-0">
                <img
                  src={value.img}
                  alt={value.title}
                  className=" w-full h-full object-contain "
                />
              </div>
              <p className=" text-slate-900 text-5xl font-extrabold text-center leading-[80px] font-sans">
                {value.title}
              </p>
              <p
                className=" text-slate-400 text-xl font-extrabold text-center font-sans break-keep"
                style={{
                  visibility: listActive[index] == 1 ? "visible" : "hidden",
                  opacity: listActive[index] == 1 ? "1" : "0",
                  transition: "opacity 0.5s ease-in 0.1s",
                }}
              >
                {value.description}
              </p>
            </li>
          ))}
        </div>
      </div>
    </div>
  );
}
