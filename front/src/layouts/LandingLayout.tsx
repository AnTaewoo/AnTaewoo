import LandingHeader from "@/components/header/LandingHeader";
import { Outlet } from "react-router-dom";

export default function MainLayout() {
  return (
    <>
      <div className="w-screen h-28 backdrop-blur-sm fixed top-0 left-0 right-0 px-16">
        <LandingHeader />
      </div>
      <div className="w-screen flex flex-col items-center">
        <Outlet />
      </div>
    </>
  );
}
