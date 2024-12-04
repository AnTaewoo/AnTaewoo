import { Link, useNavigate } from "react-router-dom";
import { Button } from "../ui/shadcn/button";
import { Input } from "../ui/shadcn/input";
import { MutableRefObject, useRef } from "react";

interface InputProps {
  type: string;
  placeholder: string;
  id: string;
  required: boolean;
}

interface DataType {
  email: string,
  password: string,
  currentPassword: string
}

const InputList: InputProps[] = [
  {
    type: "email",
    placeholder: "Email",
    id: "email",
    required: true,
  },
  {
    type: "password",
    placeholder: "Password",
    id: "password",
    required: true,
  },
  {
    type: "password",
    placeholder: "Current Password",
    id: "currentPassword",
    required: false,
  }
]

export default function SignupForm() {
  const inputRef: MutableRefObject<Element[]> = useRef([]);
  const nav = useNavigate();
  
  const setInputRef = (index: number) => (el: Element) => {
    inputRef.current[index] = el;
  };

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const data: DataType = {
      email: "",
      password: "",
      currentPassword: ""
    };
    InputList.map((value, index) => data[value.id] = (inputRef.current[index] as HTMLInputElement).value);

    const isSignup: boolean = signup()



  }
  return (
  <form className="w-full max-w-xl rounded-xl shadow-2xl p-5" onSubmit={(e)=>handleSubmit(e)}>
    <div className="space-y-4">
      {InputList.map((input, index) => (
        <div key={index} className="flex h-14">
          <Input type={input.type} placeholder={input.placeholder} className="w-full h-full font-bold rounded-xl pl-5 !text-lg placeholder:text-slate-400 focus:border-[#2563eb] focus:border-2" required={input.required} ref={setInputRef(index)} />
        </div>
      ))}
      <div className="flex h-14">
        <Button type="submit" className="w-full h-full bg-[#2563eb] hover:bg-[#1d4ed8] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#2563eb] transition-colors rounded-xl text-slate-50 text-xl font-bold">회원가입</Button>
      </div>
      <div className="h-10 flex items-center w-full">
        <hr className="border-gray border-2 w-full"/>
      </div>
      <div className="flex h-14">
        <Link to="/auth/signin" className="w-full h-full bg-[#3b5998] hover:bg-[#2f477a] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#3b5998] transition-colors rounded-xl text-slate-50 text-xl font-bold items-center flex justify-center">로그인으로 돌아가기</Link>
      </div>
    </div>
  </form>
  );
}