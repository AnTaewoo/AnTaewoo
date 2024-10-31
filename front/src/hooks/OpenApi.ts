import axios from "axios";

export default function OpenApi() {
  console.log(import.meta.env.VITE_OPENAI_API);
  const data = {
    model: "gpt-3.5-turbo",
    messages: [{ role: "user", content: "Say this is a test!" }],
    temperature: 0.1,
  };

  axios
    .post("https://api.openai.com/v1/chat/completions", data, {
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${import.meta.env.VITE_OPENAI_API}`, // 환경 변수를 사용하여 API 키를 설정
      },
    })
    .then((response) => {
      console.log(response.data);
    })
    .catch((error) => {
      console.error(error);
    });
}
