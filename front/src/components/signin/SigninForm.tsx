import { Button } from "@/components/ui/shadcn/button";
import { Input } from "@/components/ui/shadcn/input";
import { MutableRefObject, useRef } from "react";
import { Link } from "react-router-dom";



export default function SigninForm() {
  const inputRef: MutableRefObject<Element[]> = useRef([]);
  
  const setInputRef = (index: number) => (el: Element) => {
    inputRef.current[index] = el;
  };

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const email = (inputRef.current[0] as HTMLInputElement).value;
    const password = (inputRef.current[1] as HTMLInputElement).value;

    const regexEmail = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    const regexPassword = /^.{8,20}$/;

    const isValidEmail = regexEmail.test(email);
    const isValidPassword = regexPassword.test(password);

    switch (true) {
      case !isValidEmail:
        alert("이메일 형식이 올바르지 않습니다.");
        break;
      case !isValidPassword:
        alert("비밀번호는 영문, 숫자를 포함한 8자 이상 20자 이하로 입력해주세요.");
        break;
      default:
        alert("로그인 성공!");
        break;
    }

  }

  return (
  <form className="w-full max-w-xl rounded-xl shadow-2xl p-5" onSubmit={(e) => handleSubmit(e)}>
    <div className="space-y-4">
      <div className="flex h-14">
        <Input type="email" placeholder="Email" className="w-full h-full font-bold rounded-xl pl-5 !text-lg placeholder:text-slate-400 focus:border-[#2563eb] focus:border-2" ref={setInputRef(0)} autoFocus={true} required={true} />
      </div>
      <div className="flex h-14">
        <Input type="password" placeholder="Password" className="w-full h-full font-bold rounded-xl pl-5 !text-lg placeholder:text-slate-400 focus:border-[#2563eb] focus:border-2" ref={setInputRef(1)} required={true} />
      </div>
      <div className="flex h-14">
        <Button type="submit" className="w-full h-full bg-[#2563eb] hover:bg-[#1d4ed8] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#2563eb] transition-colors rounded-xl text-slate-50 text-xl font-bold">로그인</Button>
      </div>
      <div className="h-10 flex items-center w-full">
        <hr className="border-gray border-2 w-full"/>
      </div>
      <div className="flex h-14">
        <Link to="/auth/signup" className="w-full h-full bg-[#3b5998] hover:bg-[#2f477a] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#3b5998] transition-colors rounded-xl text-slate-50 text-xl font-bold items-center flex justify-center">새 계정 만들기</Link>
      </div>
    </div>
  </form>)
}