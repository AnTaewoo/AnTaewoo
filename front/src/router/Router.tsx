import { createBrowserRouter } from "react-router-dom";
import LandingLayout from "@/layouts/LandingLayout";
import Landing from "@/pages/landing/Landing";

export const router = createBrowserRouter([
  {
    path: "",
    element: <LandingLayout />,
    children: [{ path: "", element: <Landing /> }],
  },
]);
