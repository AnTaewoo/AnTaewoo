interface Proptype {
  email: string;
  password: string;
  currentPassword: string;
}

const signup = ({email,password,currentPassword}: Proptype): boolean => {
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
        return true;
    }

    return false;
}