import { Link, useNavigate } from "react-router-dom";
import { Button } from "../ui/shadcn/button";
import { Input } from "../ui/shadcn/input";
import { MutableRefObject, useRef } from "react";

const InputList = [
  {
    type: "email",
    placeholder: "Email",
    required: true,
  },
  {
    type: "password",
    placeholder: "Password",
    required: true,
  },
  {
    type: "password",
    placeholder: "Current Password",
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
    const email = (inputRef.current[0] as HTMLInputElement).value;
    const password = (inputRef.current[1] as HTMLInputElement).value;
    const currentPassword = (inputRef.current[2] as HTMLInputElement).value;

    const regexEmail = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    const regexPassword = /^.{8,20}$/;
    const regexCurrentPassword = password === currentPassword;

    const isValidEmail = regexEmail.test(email);
    const isValidPassword = regexPassword.test(password);
    const isValidCurrentPassword = regexCurrentPassword;

    switch (true) {
      case !isValidEmail:
        alert("이메일 형식이 올바르지 않습니다.");
        break;
      case !isValidPassword:
        alert("비밀번호는 영문, 숫자를 포함한 8자 이상 20자 이하로 입력해주세요.");
        break;
      case !isValidCurrentPassword:
        alert("비밀번호가 일치하지 않습니다.");
        break;
      default:
        alert("회원가입 성공!");
        // backend logic
        nav("/auth/signin");
        break;
    }

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