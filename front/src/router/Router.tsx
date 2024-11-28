import { createBrowserRouter } from "react-router-dom";
import LandingLayout from "@/layouts/LandingLayout";
import Landing from "@/pages/landing/Landing";
import AuthLayout from "@/layouts/AuthLayout";
import Signin from "@/pages/signin/Signin";
import Signup from "@/pages/signup/Signup";

export const router = createBrowserRouter([
  {
    path: "",
    element: <LandingLayout />,
    children: [{ path: "", element: <Landing /> }],
  },
  {
    path: "auth",
    element: <AuthLayout />,
    children: [
      { path: "signin", element: <Signin /> },
      { path: "signup", element: <Signup /> },
    ],
  },
]);
