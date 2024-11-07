import { useContext } from "react";
import LandingContext from "@/context/LandingContext";
import Overview from "./container/Overview";
import About from "./container/About";
import Contact from "./container/Contact";
import Main from "./container/Main";

export default function Landing() {
  const landingCtx = useContext(LandingContext);
  const ElementList = [
    { title: "Main", element: <Main /> },
    { title: "Overview", element: <Overview /> },
    { title: "About", element: <About /> },
    { title: "Contact", element: <Contact /> },
  ];

  return (
    <div className=" w-full bg-[#0E002D]">
      {ElementList.map((value, index) => (
        <div ref={(e) => (landingCtx.scrollRef.current[index] = e)} key={index}>
          {value.element}
        </div>
      ))}
    </div>
  );
}
