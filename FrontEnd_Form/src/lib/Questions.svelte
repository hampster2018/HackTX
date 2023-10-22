<!-- https://cf62-198-214-81-247.ngrok-free.app/getDailyQuestions -->

<script lang="ts">
    import { onMount } from "svelte";
    import API_KEY from "./APIKEY";
    import { questions } from "./store";

    let url="https://highly-boss-dodo.ngrok-free.app/getDailyQuestions"

    onMount(async () => {
        fetch(url, {
            method: "get",
            headers: new Headers({
                "ngrok-skip-browser-warning": "69420",
                "Authorization": API_KEY,
            }),
            })
      .then((response) => response.json())
      .then((data) => {
        if (data.length == 0) {
          questions.set(["How are you feeling today?"]);
        }
        else {
            questions.set(data);
        }
    })
      .catch((err) => console.log("Error:" + err));
        console.log(questions)
    });

    
</script>