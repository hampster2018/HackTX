<script lang="ts">
    import { onMount } from 'svelte'
    import App from '../App.svelte'
    import { fade } from 'svelte/transition'

    let q_txt = "Have you been able to talk with your friends recently?"
    let ans1 = "I've been able to talk with them regularly"
    let ans2 = "I've been able to talk with them sometimes"
    let ans3 = "I haven't been able to talk with them recently"

    let ready = false;
    onMount(() => ready = true);

    export const user = () => console.log('test');
</script>

<main class="ci-quick">
    <div class="ci-container">
        <div class="te"></div>
        <p>{q_txt}</p>
    </div>
    <div class="ci-ans-container">
        <button class="ans" id="ans-pos">{ans1}</button>
        <button class="ans" id="ans-neu">{ans2}</button>
        <button class="ans" id="ans-neg">{ans3}</button>
    </div>


    
</main>

<style>
    .ci-ans-container{
        /* display: flex; */
    }

    .ans{
        width: 100%;
        margin-top: 6%;
        /* margin: 2%; */
        border: solid #81BE1C;
        color: white;
    }

    .ci-container{
        /* border: solid 1px; */
        border-radius: 7px;
        margin-bottom: 20px;
        color: black;
        /* background-color: rgb(250, 250, 250); */
        border: solid 1px white;
        box-shadow:4px 4px 4px 5px rgba(5, 5, 82, 0.05);
        border-radius: 4px;
        width: 100%;
        min-height: 75px;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        font-size: 150%;
        /* display: inline; */
        /* justify-content: inline; */
        
    }

    #ans-pos{
        background-color: #81BE1C;
    }

    #ans-pos:focus{
        background-color: #5b8615;
    }

    #ans-neu{
        background-color: #81BE1C;
    }

    #ans-neu:focus{
        background-color: #5b8615;
    }

    #ans-neg{
        background-color: #81BE1C;
    }

    #ans-neg:focus{
        background-color: #5b8615;
    }
</style>