import API_KEY from "./APIKEY";

let url="https://loved-crawdad-privately.ngrok-free.app/postDailyAnswer"

function postAnswer(id : string, question : string, answer : string) {

    console.log("hello")

    const formData = new FormData()
    formData.append("id", id)
    formData.append("question", question)
    formData.append("answer", answer)

    fetch(url, {
        method: 'post',
        headers: new Headers({
            'ngrok-skip-browser-warning': '69420',
            'Authorization': API_KEY,
        }),
        body: formData,
    })
    .catch((err) => console.log("Error:" + err));

}

export default postAnswer;