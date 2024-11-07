import bgImage from "@/assets/background.png";
import { Button } from "@/components/ui/button";
import LandingContext from "@/context/LandingContext";
import { useContext } from "react";

export default function Main() {
  const handleScrollView = useContext(LandingContext).handleScrollView;
  return (
    <div className=" w-screen">
      <div className="w-full h-screen bg-[#0E002D] -z-10">
        <img
          src={bgImage}
          alt="background"
          className=" w-full h-full bg-cover"
        />
      </div>
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-[calc(50%+2rem)] flex flex-col items-center">
        <p className="text-7xl text-slate-50 font-bold text-center leading-[80px]">
          Track Your TIME
          <br />
          Purely For Yourself
        </p>
        <p className="text-xl font-sans text-slate-50 text-center mt-5">
          AI가 다양한 방해 요소를 분석하여, 집중해서 공부한 시간만을 정확하게
          측정합니다
        </p>
        <div className="flex gap-6">
          <Button
            className="h-full hover:scale-105  hover:text-slate-50 transition-all mt-16 border-white border-2 bg-white rounded-full w-40"
            variant="default"
          >
            <p className="text-base font-bold p-2">Start!</p>
          </Button>
          <Button
            className="h-full text-slate-50 hover:scale-105  hover:text-slate-50 transition-all mt-16 border-white border-2 rounded-full w-40"
            variant="outline"
            onClick={() => handleScrollView(1)}
          >
            <p className="text-base font-bold p-2">Overview</p>
          </Button>
        </div>
      </div>
    </div>
  );
}
