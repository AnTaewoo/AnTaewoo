import { useContext } from "react";
import LandingContext from "@/provider/context/LandingContext";
import Overview from "@/components/landing/Overview";
import About from "@/components/landing/About";
import Main from "@/components/landing/Main";

export default function Landing() {
  const landingCtx = useContext(LandingContext);
  const ElementList = [
    { title: "Main", element: <Main />, bgColor: "bg-[#0E002D]" },
    { title: "Overview", element: <Overview />, bgColor: "bg-[#0E002D]" },
    { title: "About", element: <About />, bgColor: "bg-[#0E002D]" },
  ];

  return (
    <div className=" w-full overflow-hidden">
      {ElementList.map((value, index) => (
        <div
          ref={(e) => (landingCtx.scrollRef.current[index] = e)}
          key={index}
          className={`w-full h-full ${value.bgColor}`}
        >
          {value.element}
        </div>
      ))}
    </div>
  );
}
