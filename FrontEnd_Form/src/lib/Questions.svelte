<!-- https://cf62-198-214-81-247.ngrok-free.app/getDailyQuestions -->

<script lang="ts">
    import { onMount } from "svelte";
    import API_KEY from "./APIKEY";
    console.log("API_KEY: " + API_KEY);

    let url="https://loved-crawdad-privately.ngrok-free.app/getDailyQuestions"
    let questions : string[] = [];

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
        console.log(data);
        questions = data
    })
      .catch((err) => console.log("Error:" + err));
        console.log(questions)
    });

    
</script>